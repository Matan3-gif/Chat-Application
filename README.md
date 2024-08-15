# Chat-Application

This project includes a chat server and a chat client implemented in Python. The chat server handles multiple client connections, manages user authentication, and broadcasts messages to all connected clients. The chat client connects to the server, allows users to authenticate, and facilitates sending and receiving messages.

## Server

### Overview
The chat server script sets up a TCP server that listens for incoming client connections, handles user authentication, and broadcasts chat messages to all connected clients.

### Features
* Socket Connection: Listens for incoming client connections on a specified IP address and port.
* User Authentication: Prompts clients for a username and password, authenticates against a predefined list.
* Message Broadcasting: Distributes chat messages from one client to all other connected clients.
* Client Management: Handles new connections, disconnections, and errors.

### Configuration
* HOST: Set to '0.0.0.0' by default to listen on all available network interfaces.
*  PORT: Default port is '61116'.

### Usage
1. Run the Server: Execute the script using Python: python chat_server.py

2.  Authentication: The server uses a predefined dictionary of usernames and passwords. Modify the users dictionary in the script to add or change credentials.

### Example Output

Chat server is listening on 0.0.0.0:61116
New connection from ('127.0.0.1', 12345)

## Client

### Overview
The chat client script connects to the chat server, allows users to log in, and provides an interface for sending and receiving messages.

### Features

* Socket Connection: Connects to the server using a specified IP address and port.
* User Authentication: Prompts for a username and password, sends them to the server.
* Chat Interface: Enables users to send and receive messages.
* Exit Command: Type /exit to leave the chat.

### Configuration
HOST: Replace with the IP address of the chat server.
PORT: Port should match the server's port (61116 by default).

### Usage
1. Run the Client: Execute the script using Python: python chat_client.py
2. Login: Enter your username and password as prompted.
3. Chat: Type messages and receive responses. Use /exit to disconnect from the chat.

###  Example Interaction
Enter your username: johndoe
Enter your password: mypassword
login successful!

> Hello, server!
Server: johndoe: Hello, server!
> /exit
You have left the chat.

## Requirements
* Python 3.x

## Notes
* Ensure the server is running before starting the client.
* Modify the server's users dictionary to manage user credentials.
* Both scripts should be run separately: start the server first, then connect clients.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

