import socket
from config import HOST, PORT

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        print("Esperando por conexión")
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada de {client_address}")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Mensaje recibido: {message}")

            if message == "DESCONEXION":
                print(f"Desconectando cliente {client_address}")
                client_socket.close()
                break
            else:
                response = message.upper()
                client_socket.send(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()