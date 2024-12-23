import socket

def start_tcp_server(host='0.0.0.0', port=9999):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socker.listen(5)
    print(f"TCP server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {data}")

        client_socket.send(f"Message received: {data}".encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    start_tcp_server()