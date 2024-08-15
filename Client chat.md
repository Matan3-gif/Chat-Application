# Client chat
This Python script implements a simple chat client that connects to a server using TCP/IP sockets. It allows users to log in with a username and password, participate in a chat session, and send messages to the server.

##  Features
* Socket Connection: Connects to a server using a specified IP address and port.
* Login Process: Prompts the user for a username and password, then sends these credentials to
  the server.
* Chat Interface: Allows the user to send and receive chat messages.
* Exit Command: Users can type /exit to leave the chat.

## Usage
1. Configuration: Update the 'HOST' and 'PORT' constants in the code with the server's IP address and port number.

2. Run the Script: Execute the script using Python. It will prompt you to enter your username and password.

3. Chat: After successful login, you can start sending messages. Type '/exit' to end the session.

## Error Handling
* Login Failure: If the login is unsuccessful, the script will print an error message and exit.
* Exceptions: Any socket-related or network errors will be caught and displayed.

## Requirements
* Python 3.x

## Notes
* Ensure that the server you are connecting to is running and correctly configured to accept connections on the specified port.
* The server should handle the login authentication and chat functionality as expected by this client script.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
