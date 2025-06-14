import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from app.connection import ConnectionHandler
import threading

class FileChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Full-Duplex File & Chat App")
        self.master.geometry("600x500")

        self.setup_gui()

        self.connection = ConnectionHandler(self)

    def setup_gui(self):
        frame = tk.Frame(self.master)
        frame.pack(pady=10)

        tk.Label(frame, text="Your Role:").grid(row=0, column=0)
        self.role_var = tk.StringVar(value="Server")
        tk.OptionMenu(frame, self.role_var, "Server", "Client").grid(row=0, column=1)

        tk.Label(frame, text="Peer IP (for Client):").grid(row=0, column=2)
        self.peer_ip_entry = tk.Entry(frame, width=15)
        self.peer_ip_entry.grid(row=0, column=3)

        self.connect_button = tk.Button(frame, text="Connect", command=self.connect)
        self.connect_button.grid(row=0, column=4, padx=5)

        self.chat_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, height=15)
        self.chat_area.pack(padx=10, pady=5)
        self.chat_area.config(state=tk.DISABLED)

        self.msg_entry = tk.Entry(self.master, width=50)
        self.msg_entry.pack(side=tk.LEFT, padx=(10, 5), pady=5)
        self.msg_entry.bind("<Return>", lambda event: self.send_message())

        tk.Button(self.master, text="Send", command=self.send_message).pack(side=tk.LEFT, padx=5)
        tk.Button(self.master, text="Send File", command=self.send_file).pack(side=tk.LEFT, padx=5)

    def log(self, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.see(tk.END)
        self.chat_area.config(state=tk.DISABLED)

    def connect(self):
        role = self.role_var.get()
        if role == "Server":
            threading.Thread(target=self.connection.start_server, daemon=True).start()
        else:
            peer_ip = self.peer_ip_entry.get().strip()
            if not peer_ip:
                messagebox.showerror("Error", "Please enter peer IP address")
                return
            threading.Thread(target=self.connection.start_client, args=(peer_ip,), daemon=True).start()

    def send_message(self):
        msg = self.msg_entry.get().strip()
        self.connection.send_message(msg)
        self.msg_entry.delete(0, tk.END)

    def send_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            self.connection.send_file(filepath)
