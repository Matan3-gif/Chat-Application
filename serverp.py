import socket
import select

# Constants
HOST = '0.0.0.0'  # Replace with the IP address of the server or '0.0.0.0' to listen on all available interfaces
PORT = 61116
BUFFER_SIZE = 2048


def main():
    try:
        # Create a socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the address and port
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Chat server is listening on {HOST}:{PORT}")

        sockets_list = [server_socket]
        clients = {}  # Dictionary to store connected clients with their usernames

        while True:
            read_sockets, _, _ = select.select(sockets_list, [], [])

            for current_socket in read_sockets:
                if current_socket == server_socket:
                    client_socket, client_address = server_socket.accept()
                    print(f"New connection from {client_address}")
                    client_socket.sendall(b"Username: ")
                    username = client_socket.recv(BUFFER_SIZE).decode().strip()

                    client_socket.sendall(b"Password: ")
                    password = client_socket.recv(BUFFER_SIZE).decode().strip()

                    if username in clients or (username in users and users[username] == password):
                        client_socket.sendall(b'login successful!\n')
                        sockets_list.append(client_socket)
                        clients[client_socket] = username
                        client_socket.sendall(f"Welcome to the chat, {username}!\n".encode())
                    else:
                        client_socket.sendall(b'Invalid username or password.\n')
                        client_socket.close()
                else:
                    try:
                        data = current_socket.recv(BUFFER_SIZE)
                        if data:
                            sender_username = clients[current_socket]
                            message = data.decode().strip()
                            broadcast_message = f"{sender_username}: {message}\n".encode()
                            for client in clients:
                                if client != server_socket and client != current_socket:
                                    client.sendall(broadcast_message)
                        else:
                            # Client disconnected
                            username = clients[current_socket]
                            print(f"{username} has left the chat")
                            broadcast_message = f"{username} has left the chat\n".encode()
                            for client in clients:
                                if client != server_socket and client != current_socket:
                                    client.sendall(broadcast_message)
                            sockets_list.remove(current_socket)
                            current_socket.close()
                            del clients[current_socket]

                    except Exception as e:
                        # Handle any errors with the client
                        username = clients[current_socket]
                        print(f"{username} has left the chat (error: {e})")
                        broadcast_message = f"{username} has left the chat (error: {e})\n".encode()
                        for client in clients:
                            if client != server_socket and client != current_socket:
                                client.sendall(broadcast_message)
                        sockets_list.remove(current_socket)
                        current_socket.close()
                        del clients[current_socket]

    except KeyboardInterrupt:
        print("Server terminated by the user.")

    finally:
        server_socket.close()


if __name__ == "__main__":
    users = {
        'user': 'password',
        'admin': 'admin',
        'orr': '12345',
        'michael': '67890',
        'matan': '98765'
    }

    main()
