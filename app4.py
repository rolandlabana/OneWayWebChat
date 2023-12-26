from flask import Flask, render_template, request
import socket
import threading

app = Flask(__name__)

# Function to handle communication with terminal-based server
def send_to_terminal(message):
    terminal_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    terminal_server.connect(('127.0.0.1', 9999))  # Adjust host and port as needed
    terminal_server.send(message.encode('utf-8'))
    terminal_server.send(b'\n')  # Add a newline character to indicate message end
    terminal_server.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    
    #print the message received to the console
    print(f"Received message from web client: {message}")

    # Start a new thread for socket communication
    communication_thread = threading.Thread(target=send_to_terminal, args=(message,))
    communication_thread.start()

    # Return a response back to the web client (modify as needed)
    return "Server received your message: " + message

if __name__ == '__main__':
    app.run(debug=True)

