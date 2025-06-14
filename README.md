# 📡 Full-Duplex File & Chat App (Tkinter + Sockets)

A Python-based desktop application that allows **two-way (full-duplex)** real-time chat and file transfer between two laptops on the **same network**, with a friendly **Tkinter GUI**.

---

## 📁 Features

- 🔁 Full-duplex chat (both users can send/receive messages at the same time)
- 📂 File transfer between systems
- 🧠 Auto handles both client/server roles
- 🖥️ Built with `Tkinter` GUI
- 🔒 Works entirely over local network (no internet required)

---

## 📦 Folder Structure

```
full_duplex_filechat/
├── app/
│   ├── __init__.py
│   ├── gui.py               # Main GUI code
│   ├── connection.py        # Socket handling
│   ├── file_transfer.py     # File send/receive logic
│   └── config.py            # App settings like port and buffer size
├── received_files/          # Stores received files
├── assets/icons/            # (Optional) For GUI assets
├── main.py                  # Entry point
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/full_duplex_filechat.git
cd full_duplex_filechat
```

### 2. (Optional but Recommended) Create Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> The app uses only the standard `tkinter` and `socket` libraries in Python 3.x. No third-party packages are required.

---

## 🚀 Run the App

```bash
python main.py
```

---

## 💡 How to Use

### 🔗 Step 1: Connect Two Laptops to Same Network (Wi-Fi or LAN)

### 🖥️ On Laptop 1 (Server)

1. Launch the app
2. Select **"Server"** from the dropdown
3. Click **Connect**
4. It will say `"[SERVER] Waiting for connection..."`

### 💻 On Laptop 2 (Client)

1. Launch the app
2. Select **"Client"**
3. Enter the IP address of Laptop 1 (You can find it using `ipconfig` or `ifconfig`)
4. Click **Connect**

---

## 💬 Chat & 📁 File Transfer

- Type messages and press **Enter** or click **Send**
- Click **Send File** to select and send any file
- Received files are saved inside the `received_files/` folder as `received_<filename>`

---

## ⚠️ Troubleshooting

| Issue | Fix |
|-------|-----|
| ❌ App not connecting | Ensure both devices are on same Wi-Fi and IP is correct |
| 🔥 Firewall blocking | Allow Python through firewall |
| 🛑 File not received | Ensure `received_files/` folder exists |
| ❗ Port in use | Change `PORT` in `config.py` on both devices |
| 📛 Unknown threading error | Make sure `import threading` is present in all relevant files |

---

## 🙋 FAQ

**Q:** Does it work over the internet?  
**A:** No, it's designed for **local LAN communication** only.

**Q:** Can I run both server and client on the same laptop for testing?  
**A:** Yes! Use `127.0.0.1` as the IP on the client.

---

## 📌 Requirements

- Python 3.7 or higher
- Tkinter (comes with Python standard library)

---

## 🛡️ License

MIT License

---

## ✨ Future Ideas

- Add username support
- Show timestamps in chat
- File transfer progress bar
- Support for folders
- Encrypted transmission
