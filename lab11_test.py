# The async parts are run with asyncio.run(...). The socket part is checked by starting
# a tiny echo server (on a spare port) inside the test and connecting your client to it.
#
# (There is no test for reverse_server.py - a server is checked by hand with client.py.)

import asyncio
import socket
import threading

from lab11 import gather_doubled, fastest, echo_once


def test_gather_doubled():
    assert asyncio.run(gather_doubled([1, 2, 3, 4])) == [2, 4, 6, 8]
    assert asyncio.run(gather_doubled([])) == []


def test_fastest():
    # B has the shortest delay, so it finishes first.
    jobs = [("A", 0.06), ("B", 0.02), ("C", 0.04)]
    assert asyncio.run(fastest(jobs)) == "B"


def _start_echo_server():
    """Start a one-shot echo server on a spare port; return the port."""
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port = srv.getsockname()[1]

    def serve():
        conn, _ = srv.accept()
        with conn:
            data = conn.recv(1024)
            conn.sendall(data)
        srv.close()

    threading.Thread(target=serve, daemon=True).start()
    return port


def test_echo_once():
    port = _start_echo_server()
    assert echo_once("127.0.0.1", port, "hello") == "hello"

    port2 = _start_echo_server()
    assert echo_once("127.0.0.1", port2, "sockets are fun") == "sockets are fun"
