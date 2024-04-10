```mermaid
sequenceDiagram;
    Client ->> +IManagedListener: connect
    IManagedListener ->> IClientConnectionManager: new client
    IClientConnectionManager ->> IClientConnectionHandler: Process
    loop Should process connection
        IClientConnectionHandler ->> IClientConnection: recv
        IClientConnection ->> IClientConnectionHandler: Packet
        IClientConnectionHandler ->> ISessionContextManager: Get Session
        ISessionContextManager ->> IClientConnectionHandler: Session
        IClientConnectionHandler ->> IPacketDecoder: Decode Packet for Session
        IPacketDecoder ->> IClientConnectionHandler: Decoded Packet
        IClientConnectionHandler ->> IChannelHandlerRouter: Packet
        IChannelHandlerRouter ->> IChannelHandler: Packet
        IChannelHandler --> ISession: Update session state
        IChannelHandler ->> IChannelHandlerRouter: Reply Packet
        IChannelHandlerRouter ->> IClientConnectionHandler: Reply Packet
        IClientConnectionHandler ->> IPacketDecoder: Encode Packet
        IPacketDecoder ->> IClientConnectionHandler: Encoded Packet
        IClientConnectionHandler ->> IClientConnection: Send Packet
        IClientConnection ->> IClientConnectionHandler: sent


        IClientConnectionHandler ->> ISession: Is Session complete
        ISession ->> IClientConnectionHandler : Yes/No

        alt is ISession is complete
            IClientConnectionHandler --> ISessionContextManager: End Session
            IClientConnectionHandler ->> ISessionContextManager: Is Multi Session?
            ISessionContextManager ->> IClientConnectionHandler: Yes/No
        end
    end

    break when the booking process fails
        IClientConnectionHandler ->> IClientConnectionManager: Close Connection
    end


```

The pattern is a but tricky and lots of concepts are stuck in a coordinator. Each packet has to wait for a return. Ideally a session and connection isn't split. The session could instead have a connection to a tcp message send queue, and the tcp session sends packets to a session queue.


Looking into IClientConnectionHandler, there exists a producer loop that:

1. reaches out the the underlaying connection to get a packet
2. interacts with a session context manager to get or create a session
3. interacts with a packet decoder to decode the packet for a session
4. sends the decoded packet to the session

Eventually the Session will send a Packet to IClientConnectionHandler then:
1. Encodes the Packet
2. Sends the Packet to the ClientConnection which (shown in the next diagram)
   1. calls the async send (which awaits for other sends to complete) and
   2. sends the packet

The send portion follows an async chain and the ISession should wait for it's send to complete. Then if something goes wrong in the send, ISession can handle the exception in whatever way it needs (e.g. setting the session is failed). Similarly, each component on the send chain can hook exceptions and do something along the way.

```mermaid
sequenceDiagram;
        loop Should process connection
        activate IClientConnectionHandler
        IClientConnectionHandler ->> IClientConnection: Get Packet
        IClientConnection -->> IClientConnectionHandler: Packet
        IClientConnectionHandler ->> +ISessionContextManager: Get Session for Packet
        ISessionContextManager ->> -IClientConnectionHandler: Session
        IClientConnectionHandler ->> +IPacketDecoder: Decode Packet for Session
        IPacketDecoder ->> -IClientConnectionHandler: Decoded Packet
        IClientConnectionHandler ->> ISession: Process
        end
        deactivate IClientConnectionHandler
        activate ISession
        ISession ->> ISession: Process
        ISession ->> IClientConnectionHandler: Send Packet
        activate IClientConnectionHandler
        IClientConnectionHandler ->> +IPacketDecoder: Encode Packet for Session
        IPacketDecoder ->> -IClientConnectionHandler: Encoded Packet
        IClientConnectionHandler ->> IClientConnection: Send Packet
        IClientConnection -->> IClientConnectionHandler: Sent or Exception
        IClientConnectionHandler -->> ISession: Sent or Exception
        deactivate IClientConnectionHandler
        deactivate ISession

```

IClientConnectionHandler communicates with an IClientConnection to get Packets. The IClietnConnection communicates with a ManagedTcpConnection (impliments IManagedConnection) to get raw bytes that make up the packet, and validates the bytes/components so that a Packet returned to the IClientConnectionHandler is valid. The ManagedTcpConnection that in turn communicates to a RawSocket (OS sepecific socket type) and handles all it's related quirks, such as empty responses, timeouts etc and either provides nothing or a entirely fulfilled request to the ManagedTcpConnection. The ManagedTcpConnection will know if the RawSocket has been disconnected, and can pass these issues up to the IClientConnectionHandler.

```mermaid
sequenceDiagram;
        IClientConnectionHandler ->> +IClientConnection: Get Packet
        IClientConnection ->> +ManagedTcpConnection: Recieve N Bytes
        ManagedTcpConnection ->> RawSocket: Read N Bytes
        RawSocket -->> ManagedTcpConnection: Bytes/Other
        ManagedTcpConnection ->> ManagedTcpConnection: Validate
        ManagedTcpConnection -->> -IClientConnection: Bytes or Exception
        IClientConnection ->> +HeaderSerialiser: Deserialise Bytes
        HeaderSerialiser ->> -IClientConnection: Header
        IClientConnection ->> +ManagedTcpConnection: Recieve N Bytes
        ManagedTcpConnection ->> RawSocket: Read N Bytes
        RawSocket -->> ManagedTcpConnection: Bytes/Other
        ManagedTcpConnection -->> -IClientConnection: Bytes or Exception
        IClientConnection ->> +Packet: Create Packet with Header and Bytes
        Packet -->> -IClientConnection: Packet
        IClientConnection -->> -IClientConnectionHandler: Packet

        IClientConnectionHandler ->> +IClientConnection: Send Packet
        IClientConnection ->> +Packet: Serialise
        Packet -->> -IClientConnection: Bytes
        IClientConnection ->> IClientConnection: Acquire Send Lock
        IClientConnection ->> +ManagedTcpConnection: Send Bytes
        ManagedTcpConnection ->> RawSocket: Send
        RawSocket -->> ManagedTcpConnection: Bytes Sent
        ManagedTcpConnection -->> -IClientConnection: Bytes Sent or Exception
        IClientConnection ->> IClientConnection: Release Send Lock
        IClientConnection -->> -IClientConnectionHandler: Sent or Exception
```
