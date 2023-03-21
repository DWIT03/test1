
import socket
from pyvncs import VNCServer

def main():
    host, port = '0.0.0.0', 5900
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[*] VNC server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[*] Connection from {addr}")

        vnc = VNCServer(client_socket)
        vnc.run()

if __name__ == "__main__":
    main()
