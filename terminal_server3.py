
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = '127.0.0.1'  # Use the same host as specified in the Flask app
port = 9999          # Use the same port as specified in the Flask app

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)  # Listen for one connection

print(f"Server listening on {host}:{port}...")

while True:

    while True:
       
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr[0]}:{addr[1]}") 

        print ("waiting for msg...")
        # Receive message from the Flask app
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            print ("no msg yet")
            break
        else:
            print ("got a msg.")
        print(f"Received message from Flask app: {message}")  # Print to server console

        # Forward the message to the terminal-based server (you would do your logic here)

        # Example: Send a response back to the Flask app
        response = "Message received by terminal server"
        client_socket.send(response.encode('utf-8'))

    # Close the client socket
    client_socket.close()

# Close the server socket (this won't be reached unless the server is terminated)
server_socket.close()

