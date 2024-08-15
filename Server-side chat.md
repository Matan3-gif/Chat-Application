# Server-side chat

This Python script implements a simple multi-client chat server using TCP/IP sockets. It supports user authentication, broadcasting messages to all connected clients,
and handling client connections and disconnections.

## Features
* Socket Connection: Listens for incoming connections on a specified IP address and port.
* User Authentication: Prompts clients for a username and password, validates them against a predefined list.
* Chat Functionality: Broadcasts messages from connected clients to all other clients.
* Client Management: Handles client connections, disconnections, and errors gracefully.

## Usage
1. Configuration: Update the HOST and PORT constants if needed. The default HOST value of 0.0.0.0 makes the server listen on all available network interfaces.
2. Run the Server: Execute the script using Python. It will start listening for incoming client connections.

### Run
typing the following: python chat_server.py

### Output Example:
Chat server is listening on 0.0.0.0:61116
New connection from ('127.0.0.1', 12345)

3. Connect Clients: Clients can connect to the server using the specified 'HOST' and 'PORT'. They will be prompted to enter a username and password.

## Authentication
* Username and Password: The server uses a predefined dictionary of users and passwords for authentication.
* Successful Login: Clients receive a welcome message and can start chatting.
* Failed Login: Clients receive an error message and are disconnected.

## Error Handling
* Client Disconnections: Handles cases where clients disconnect unexpectedly or due to errors.
* Broadcast Errors: Notifies all clients when an error occurs with a client.

## Requirements
* Python 3.x

## Notes
* Ensure that the users dictionary contains valid usernames and passwords. This is where authentication credentials are stored.
* The server will broadcast chat messages and handle multiple client connections concurrently.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
