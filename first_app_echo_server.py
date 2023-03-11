from typing import List, Tuple

import selectors
import socket

selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)

selector.register(server_socket, selectors.EVENT_READ)

try:
    while True:
        events: List[Tuple[selectors.SelectorKey, int]] = selector.select(timeout=1)

        if len(events) == 0:
            print("No Events, wait...")

        for event, _ in events:
            event_socket = event.fileobj

            if event_socket == server_socket:
                connection, client_address = server_socket.accept()
                connection.setblocking(False)
                print(f"Connection {client_address}")
                selector.register(connection, selectors.EVENT_READ)
            
            else:
                data = event_socket.recv(1024)
                print(f"Data: {data}")
                event_socket.sendall(data)

finally:
    server_socket.close()
