import socket
from config import HOST, PORT

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"Conectando al servidor en {HOST}:{PORT}")

    while True:
        message = input("Ingrese un mensaje (o 'DESCONEXION' para terminar): ")
        client_socket.send(message.encode('utf-8'))

        if message == "DESCONEXION":
            print("Solicitado desconexión del servidor")
            client_socket.close()
            break
        else:
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    start_client()