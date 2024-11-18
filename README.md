# 📨 MessageReceiver

A simple TCP and UDP server for receiving and echoing messages. Perfect for red team testing and learning network communication basics. 🚀

---

## 🌟 Features

- **TCP Server**: Listens for client connections and echoes received messages.
- **UDP Server**: Handles datagrams and sends acknowledgments.
- **Customizable**: Easily modify host and port settings.

---

## 🛠️ Getting Started

Follow these steps to set up and run the project.

### 1. **Clone the Repository**
```bash
git clone https://github.com/gilirene2/MessageRec_Python.git
cd MessageReceiver
```
### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```
### 3. Run the TCP Server
```bash
python tcp_server.py
```
### 4. Run the UDP Server
```bash
python udp_server.py
```

