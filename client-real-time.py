import socket
import time
import numpy as np

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = 'rp-f071ce.local'
    port = 9999

    # Connection to hostname on the port.
    client_socket.connect((host, port))

    with open('bitstream-3.csv', 'a') as file:
        try:
            t = time.time()
            while True:
                # Receive the data
                bit = client_socket.recv(1)
                tim = time.time()
                if not bit:
                    print("Connection closed by the server.")
                    break

                # Convert the received byte to a bit (1 or 0)
                received_bit = int.from_bytes(bit, byteorder='big')
                
                print("Received bit:", received_bit," Time: ",np.round((tim-t),5))


                # Write the bit to the file
                file.write(str(received_bit) +','+str(np.round((tim-t),5))+'\n')

        except ConnectionResetError:
            print("Server disconnected")

if __name__ == "__main__":
    start_client()
