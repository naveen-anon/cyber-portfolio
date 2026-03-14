## 🧠 Cyber Portfolio – Matrix OSINT Dashboard

A Matrix-style cyber intelligence dashboard built with Python Flask that provides multiple OSINT investigation tools in a hacker-style interface.

This project combines OSINT tools, Shodan intelligence, AI investigation reports, and a Matrix UI to simulate a cyber investigation environment.

---

⚡ Features

- 🌌 Matrix style hacker interface
- 🔎 Username investigation (Sherlock integration)
- 🛰 Shodan intelligence lookup
- 🌍 Cyber attack globe visualization
- 🕸 Maltego-style investigation graph
- 🔎 Domain OSINT lookup
- 🧠 AI-generated OSINT investigation reports
- 📊 Cyber investigation dashboard

---

## 📂 Project Structure

cyber-portfolio/

app.py
config.py
requirements.txt

modules/
    username_scan.py
    shodan_lookup.py
    osint_engine.py
    graph_builder.py
    attack_map.py
    ai_report.py

templates/
    dashboard.html

static/
    style.css
    matrix.js
    dashboard.js
    globe.js

---

## 🚀 Installation

Clone the repository

git clone https://github.com/naveen-anon/cyber-portfolio.git
cd cyber-portfolio

Install dependencies

pip install -r requirements.txt

---

## ⚙ Configuration

Edit "config.py" and add your API keys.

SHODAN_API = "YOUR_SHODAN_API_KEY"
OPENAI_API = "YOUR_OPENAI_API_KEY"
SECRET_KEY = "matrix_osint_secret"

---

## ▶ Run the Project

python app.py

## Open the dashboard in your browser

http://127.0.0.1:5000

---

## 🧪 Usage

1️⃣ Username Investigation

1. Enter a username in the Username Investigation field
2. Click Scan
3. Sherlock will search the username across multiple platforms

# Example:

username: naveen_anon

---

## 2️⃣ Shodan Lookup

1. Enter an IP address
2. Click Search
3. The tool will return Shodan intelligence data

Example:

8.8.8.8

---

## 3️⃣ Domain OSINT

1. Enter a domain name
2. Click Lookup
3. The tool will return OSINT data about the domain

Example:

example.com

---

## 4️⃣ AI Investigation Report

1. Run any investigation (username / domain / IP)
2. Click Generate Report
3. The AI will generate a cyber intelligence style report

---

## 5️⃣ Investigation Graph

The system automatically creates a Maltego-style relationship graph connecting:

- Target
- Email
- IP
- Domain
- Username

---

## 🔌 API Endpoints

Endpoint| Description
"/username"| Sherlock username investigation
"/shodan"| Shodan host intelligence
"/domain"| Domain OSINT lookup
"/graph"| Investigation relationship graph
"/attacks"| Cyber attack map data
"/report"| AI investigation report

---

## 🛠 Technologies Used

- Python
- Flask
- Sherlock
- Shodan API
- OpenAI API
- JavaScript
- Matrix animation (Canvas)

---

## ⚠ Security Notice

Do not expose API keys publicly in GitHub repositories.
Use ".env" files or environment variables for production deployments.

---

## 🧠 Future Improvements

- 🌍 Real-time global cyber attack map
- 🛰 Shodan attack visualization
- 🔎 Email breach lookup
- 📱 Phone OSINT investigation
- 🧠 AI automated OSINT reports
- 🕵 500+ site username scanner UI

---

## 👨‍💻 Author

Naveen
Cyber Security Enthusiast | OSINT Research

## GitHub:
https://github.com/naveen-anon
