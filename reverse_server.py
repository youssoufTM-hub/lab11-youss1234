# Part 4 (STRETCH) - a TCP server that sends back the REVERSED message.
#
# There is no automated test for this - run it, then connect with the provided
# client.py (in another terminal) to check it, and show it to your lab instructor.
#
# The socket setup is written for you; fill in the one TODO.

import socket

HOST, PORT = "127.0.0.1", 50011


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Listening on {HOST}:{PORT} (Ctrl-C to stop)")

    while True:
        conn, addr = server.accept()
        with conn:
            data = conn.recv(1024)
            if not data:
                continue
            # TODO: send the message back REVERSED. `data` is bytes, e.g. b"hello".
            #   Turn it into text, reverse it, and send the reversed text back with
            #   conn.sendall(...). Example: "hello" -> "olleh".
            pass


if __name__ == "__main__":
    main()
