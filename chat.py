import socket
import threading 
import argparse

def receive_messages(sock):
  while True:
    try:
      data, addr = sock.recvfrom(1024)
      print(f"\nReceived: {data.decode('utf-8')}")
    except Exception as e:
      print(f"Error receiving data: {e}")
      break

def main():
  parser = argparse.ArgumentParser(description="Chat Client")
  parser.add_argument("--remote_address", required=True, help="Remote IP address to send messages to")
  parser.add_argument("--remote_port", type=int, required=True, help="Remote port to send messages to")
  parser.add_argument("--local_port", type=int, required=True, help="Local port to listen for messages")
  args = parser.parse_args()

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind(("0.0.0.0", args.local_port))
  

  threading.Thread(target=receive_messages, args=(sock, ), daemon=True).start()

  print(f"Chat client started. Listening on port {args.local_port}")
  print(f"Sending messages to {args.remote_address}:{args.remote_port}")
  print(f"Type your message and press Enter to send. Type 'exit' to quit")

  while True:
    message = input("You: ")
    if message.lower() == "exit":
      print("Exiting chat...")
      break

    sock.sendto(message.encode("utf-8"), (args.remote_address, args.remote_port))

  sock.close()

if __name__ == "__main__":
  main()