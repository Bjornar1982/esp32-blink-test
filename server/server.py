import socket

HOST = "0.0.0.0"   # Lytt på alle nettverksgrensesnitt
PORT = 5000        # Portnummer (må matche ESP32 senere)

def start_server():
    # Opprett TCP-socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Tillat rask restart av server
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind socket til IP og port
    server_socket.bind((HOST, PORT))

    # Start lytting (maks 1 klient om gangen)
    server_socket.listen(1)

    print(f"[SERVER] Lytter på port {PORT}...")

    # Vent på klient (ESP32)
    conn, addr = server_socket.accept()
    print(f"[SERVER] Tilkoblet fra {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            print("[SERVER] Klient koblet fra")
            break

        message = data.decode().strip()
        print(f"[MOTTATT] {message}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
