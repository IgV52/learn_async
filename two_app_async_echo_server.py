from typing import List

import asyncio, signal
import socket
import logging

async def echo(connection: socket,loop: asyncio.AbstractEventLoop) -> None:
    
    try:
        while data := await loop.sock_recv(connection, 1024):
            print(f"Полученные данные {data}")
            if data == b"boom\r\n":
                raise Exception("BIG BOOM!!!")
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()

echo_tasks = []

async def listen_for_connection(server_socket: socket, 
                                loop: asyncio.AbstractEventLoop):

    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Request connect {address}")
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)

class GreacefulExit(SystemExit):
    pass

def shutdown():
    raise GreacefulExit()

async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass

async def main(loop: asyncio.AbstractEventLoop):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    for signame in {"SIGINT", "SIGTERM"}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)

    await listen_for_connection(server_socket, loop)

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main(loop))
except GreacefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()