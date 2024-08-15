import socket

# Constants
HOST = '109.65.91.222'  # Replace with the IP address of the server
PORT = 61116
BUFFER_SIZE = 2048


def main():
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((HOST, PORT))

    try:
        # Login process
        print(client_socket.recv(BUFFER_SIZE).decode())  # Welcome message
        username = input("Enter your username: ")
        client_socket.sendall(username.encode())  # Send the entered username to the server

        print(client_socket.recv(BUFFER_SIZE).decode())  # Password request
        password = input("Enter your password: ")
        client_socket.sendall(password.encode())  # Send the entered password to the server

        login_response = client_socket.recv(BUFFER_SIZE).decode()  # Receive the login response from the server
        if "login successful!" not in login_response:
            print("Login failed. Exiting.")
            client_socket.close()  # Close the client socket if login failed
            return

        # Connected and authenticated
        print(login_response)

        # Start the chat loop
        while True:
            message = input("> ")  # Read user input as the chat message
            client_socket.sendall(message.encode())  # Send the message to the server

            if message.lower() == "/exit":
                print("You have left the chat.")
                break

            response = client_socket.recv(BUFFER_SIZE).decode()  # Receive the response from the server
            print(response)  # Print the received message from the server

        # Close the client socket
        client_socket.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
