import random
import socket
import time


def main():
    host = "127.0.0.1"
    port = 9000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)
        print(f"fake sensor server listening on {host}:{port}")

        while True:
            conn, addr = server.accept()
            print(f"client connected: {addr}")
            battery = 100.0
            with conn:
                while True:
                    timestamp_ms = int(time.time() * 1000)
                    temperature = 36.5 + random.uniform(-0.5, 0.5)
                    battery = max(0.0, battery - 0.05)
                    velocity = 0.4 + random.uniform(-0.1, 0.1)
                    line = f"{timestamp_ms},{temperature:.2f},{battery:.2f},{velocity:.2f}\n"
                    conn.sendall(line.encode("utf-8"))
                    time.sleep(0.1)


if __name__ == "__main__":
    main()

