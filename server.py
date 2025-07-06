import socket
import ssl

HOST = '0.0.0.0'
PORT = 12345

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
context.load_verify_locations(cafile="ca.crt")
context.verify_mode = ssl.CERT_REQUIRED  # richiede certificato client

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"Server in ascolto su {HOST}:{PORT}")

    with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            print(f"Connessione accettata da {addr}")
            try:
                data = conn.recv(1024)
                print(f"Ricevuto: {data.decode()}")
                conn.sendall(b"Accesso consentito con mTLS!\n")
            except Exception as e:
                print("Errore nella connessione:", e)
            finally:
                conn.close()

