import socket
import threading
from app.config import PORT, BUFFER_SIZE, SEPARATOR
from app.file_transfer import receive_file

class ConnectionHandler:
    def __init__(self, gui):
        self.gui = gui
        self.conn = None
        self.addr = None
        self.sock = None

    def start_server(self):
        self.sock = socket.socket()
        self.sock.bind(("", PORT))
        self.sock.listen(1)
        self.gui.log("[SERVER] Waiting for connection...")
        self.conn, self.addr = self.sock.accept()
        self.gui.log(f"[SERVER] Connected to {self.addr}")
        threading.Thread(target=self.receive_data, daemon=True).start()

    def start_client(self, ip):
        try:
            self.conn = socket.socket()
            self.conn.connect((ip, PORT))
            self.gui.log(f"[CLIENT] Connected to {ip}:{PORT}")
            threading.Thread(target=self.receive_data, daemon=True).start()
        except Exception as e:
            self.gui.log(f"[CLIENT] Connection failed: {e}")

    def send_message(self, msg):
        if msg and self.conn:
            try:
                self.conn.send(f"MSG{SEPARATOR}{msg}".encode())
                self.gui.log(f"You: {msg}")
            except Exception as e:
                self.gui.log(f"[ERROR] Failed to send message: {e}")

    def send_file(self, filepath):
        if self.conn:
            from app.file_transfer import send_file
            send_file(self.conn, filepath, self.gui.log)

    def receive_data(self):
        while True:
            try:
                header = self.conn.recv(BUFFER_SIZE).decode()
                if header.startswith("MSG"):
                    _, msg = header.split(SEPARATOR, 1)
                    self.gui.log(f"Peer: {msg}")
                elif header.startswith("FILE"):
                    receive_file(self.conn, header, self.gui.log)
            except Exception as e:
                self.gui.log(f"[ERROR] {e}")
                break
