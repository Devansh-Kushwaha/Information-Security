import socket
import random
HOST = '127.0.0.1'  # Server's IP address
PORT = 65432        # Must match the server's port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "Requesting Key Exchange"
print("Requesting Key Exchange")
client_socket.sendall(message.encode())
while True:
    data = client_socket.recv(1024)
    if data.decode()=="Request accepted":
        P = int(client_socket.recv(1024).decode())
        G = int(client_socket.recv(1024).decode())
        print("Prime Number P=",P,"Generator G=",G)
        X=random.choice(range(P))
        R1=(G**X)%P
        client_socket.sendall(str(R1).encode())
        R2 = int(client_socket.recv(1024).decode())
        print("R2=",R2)
        SecretKey=(R2**X)%P
        print("Symmetric Key is",SecretKey)
client_socket.close()
