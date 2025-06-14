import os
from app.config import BUFFER_SIZE, SEPARATOR

def send_file(conn, filepath, log_fn):
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    try:
        conn.send(f"FILE{SEPARATOR}{filename}{SEPARATOR}{filesize}".encode())
        with open(filepath, "rb") as f:
            while chunk := f.read(BUFFER_SIZE):
                conn.sendall(chunk)
        log_fn(f"[FILE SENT] {filename} ({filesize} bytes)")
    except Exception as e:
        log_fn(f"[ERROR] Failed to send file: {e}")

def receive_file(conn, header, log_fn):
    _, filename, filesize = header.split(SEPARATOR)
    filesize = int(filesize)
    log_fn(f"[RECEIVING FILE] {filename} ({filesize} bytes)")

    with open("received_files/received_" + filename, "wb") as f:
        received = 0
        while received < filesize:
            data = conn.recv(min(BUFFER_SIZE, filesize - received))
            if not data:
                break
            f.write(data)
            received += len(data)
    log_fn(f"[FILE RECEIVED] saved as received_{filename}")
