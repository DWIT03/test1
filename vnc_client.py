
import socket
from pyvncs import VNCClient

def main():
    host, port = '127.0.0.1', 5900
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"[*] Connected to VNC server at {host}:{port}")

    vnc = VNCClient(client_socket)
    vnc.run()

if __name__ == "__main__":
    main()
