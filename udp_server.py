import socket

def start_udp_server(host='0.0.0.0', port=9999):
    server_socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP server listening on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received from {client_address}: {data.decode('utf-8')}")

        server_socket.sendto(b"Message received", client_address)

if __name__ == "__main__":
    start_udp_server()