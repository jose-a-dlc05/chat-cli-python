import socket

HOST = "127.0.0.1" # Standard loopback interface address (localhost)
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    print(f"Connected by {addr}")
    while True:
      data = conn.recv(1024)
      if not data:
        break
      conn.sendall(data)

# socket.socket() creates a socket object that supports the context manager type, so you can use it in a with statement.
# The arguments passed to socket() are constants used to specify the address family and socket type. AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.