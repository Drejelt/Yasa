import socket
from CaesarsCipher import Caesar #pip install CaesarsCipher

def start_server_tcp(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP Socket listening on {host}:{port}")

        connection, addr = server_socket.accept()
        with connection:
            print(f"Connected with Client({addr})")
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                received_message = data.decode()
                print(f"Received: {received_message} from {addr}")
                client_key, message = received_message.split(":", 1)
                key = int(client_key)

                encrypted_message = Caesar.encrypt(message, key)
                response = f"Server response: {encrypted_message}"
                connection.sendall(response.encode())

if __name__ == "__main__":
    start_server_tcp()
