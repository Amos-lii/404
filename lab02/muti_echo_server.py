import socket
from multiprocessing import Process
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def main():

    #create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # reuse port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)

        while True:

            conn, addr = s.accept()
            #start deamon for multiple connections
            p = Process(target=handle_echo, args=(conn, addr))
            p.daemon = True
            p.start()
            print("Start process:", p)


def handle_echo(addr, conn):
    print("Connected by", addr)
    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_DOWN)
    conn.close()


if __name__ == "__main__":
    main()