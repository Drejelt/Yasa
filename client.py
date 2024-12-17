import socket
from colorama import Fore, Style
def start_client_tcp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = input(f"Enter message (format: {Fore.GREEN}key:{Fore.YELLOW}message{Style.RESET_ALL}): ")
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024)
        print(f"\tEcho from server: \n{response.decode()}")


if __name__ == "__main__":
    start_client_tcp("127.0.0.1", 65432)
