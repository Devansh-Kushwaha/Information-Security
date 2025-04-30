import socket
import random
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on
primeList=[]
for i in range(2,100):
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            break
    else:
        primeList.append(i)
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        rec_message=data.decode()
        if rec_message=="Requesting Key Exchange":
            print("Request accepted")
        conn.sendall(b"Request accepted")
        # P=random.choice(primeList[5:])
        P=19
        EulersTotient=P-1   #Finding Primitive rrot for G
        PrimeFactors=[]
        for i in primeList:
            if i>=P:
                break
            elif EulersTotient%i==0:
                PrimeFactors.append(i)

        PrimitiveRoots=[]
        for g in range(1,P):
            for q in PrimeFactors:
                temp=g**((EulersTotient)/q)
                temp=temp%P
                if temp==1:
                    break
            else:
                PrimitiveRoots.append(g)

        G=random.choice(PrimitiveRoots)

        conn.sendall(str(P).encode())

        conn.sendall(str(G).encode())
        Y=random.choice(range(P))
        R2=(G**Y)%P
        R1 = int(conn.recv(1024).decode())
        conn.sendall(str(R2).encode())
        print("R1=",R1)
        SecretKey=(R1**Y)%P
        print("Symmetric Key is",SecretKey)
    conn.close()
