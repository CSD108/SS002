import socket
import numpy as np
import time

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = 'rp-f071ce.local'
    port = 9995

    # Connection to hostname on the port.
    client_socket.connect((host, port))

    # Buffer size for receiving the array
    buffer_size = 163840 * 12  # 4 bytes for each float32 element
    timestamp = 0
    while True:
        # Receive the data
        data = b''
        while len(data) < buffer_size:
            packet = client_socket.recv(buffer_size - len(data))
            if not packet:
                break
            data += packet

        if len(data) < buffer_size:
            print("Connection closed by the server.")
            break

        # Convert bytes back to numpy array
        array = np.frombuffer(data, dtype=np.float32)

        print("Received array of length", len(array))

        # Store the array in a file with a timestamp
         
        filename = f"samples_array_{timestamp}.txt"
        timestamp +=10
        np.savetxt(filename, array, fmt='%f')
        print(f"Saved array to {filename}")

if __name__ == "__main__":
    start_client()
