# 🛡️ NetScope Analyzer

A simple and interactive **Network Packet Sniffer** built using **Python, Flask, and Scapy**. This project captures live network packets and displays important packet information such as **Source IP**, **Destination IP**, and **Protocol** through a user-friendly web dashboard.

---

## 📌 Project Overview

NetScope Analyzer is designed to monitor network traffic in real time. It helps users understand how data packets travel across a network by capturing and displaying essential packet details.

This project was developed as part of the **CodeAlpha Cyber Security Internship**.

---

## ✨ Features

- 📡 Live network packet capture
- 🌐 Displays Source IP Address
- 🎯 Displays Destination IP Address
- 🔍 Identifies packet protocols (TCP, UDP, ICMP)
- 💻 Interactive web dashboard using Flask
- ⚡ Lightweight and easy to use

---

## 🛠️ Technologies Used

- Python 3.13
- Flask
- Scapy
- HTML5
- CSS3
- JavaScript
- Npcap (Windows)

---

## 📂 Project Structure

```
NetScopeAnalyzer/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── packet_sniffer.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/VINOTHINI-006/NetScopeAnalyzer.git
```

### 2️⃣ Navigate to the Project

```bash
cd NetScopeAnalyzer
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Npcap

Download and install **Npcap** from:

https://npcap.com/

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

![Screenshot(14)](Screenshot/Screenshot(14).png)

## 🔄 Workflow

```
Network Traffic
       │
       ▼
Scapy Packet Capture
       │
       ▼
Packet Processing
       │
       ▼
Flask Backend
       │
       ▼
Web Dashboard
```

---

## 🚀 Future Enhancements

- Packet filtering by protocol
- Export captured packets to CSV
- Packet search functionality
- Real-time graphical traffic analysis
- User authentication
- Dark/Light mode
- Live packet statistics
- Packet logging database

---

## 📚 Learning Outcomes

- Network Packet Analysis
- Flask Web Development
- Python Programming
- Scapy Packet Sniffing
- Cybersecurity Fundamentals
- Web Dashboard Development

---

## 👩‍💻 Author

**VINOTHINI V**

GitHub: https://github.com/VINOTHINI-006

LinkedIn: *(Add your LinkedIn profile here)*

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

**CodeAlpha Cyber Security Internship Project**
