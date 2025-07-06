import socket
import ssl

HOST = 'server'
PORT = 12345

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile="ca.crt")
context.load_cert_chain(certfile="client.crt", keyfile="client.key")

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.sendall(b"Ciao server, sono client con certificato!\n")
        data = ssock.recv(1024)
        print(f"Risposta server: {data.decode()}")

