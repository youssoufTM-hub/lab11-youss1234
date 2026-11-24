# A little client for testing your reverse_server.py (Part 4). This is complete - you
# don't need to change it.
#
# Usage (with reverse_server.py already running in another terminal):
#     python client.py hello
# It should print:  olleh

import socket
import sys

HOST, PORT = "127.0.0.1", 50011


def main():
    message = sys.argv[1] if len(sys.argv) > 1 else "hello"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode())
        reply = s.recv(1024)
    print(reply.decode())


if __name__ == "__main__":
    main()
