# 🧠 Cyber Portfolio – Matrix OSINT Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![OSINT](https://img.shields.io/badge/Category-OSINT-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Matrix-style OSINT investigation dashboard built with Python Flask.

This project combines multiple cyber intelligence tools into a single interface including username investigation, Shodan intelligence, domain OSINT, cyber attack visualization, and AI-generated investigation reports.

---

## 🚀 Features

- Matrix hacker style dashboard UI
- Username investigation using Sherlock
- Shodan host intelligence lookup
- Cyber attack globe visualization
- Maltego-style investigation graph
- Domain OSINT lookup
- AI-generated investigation reports
- Cyber investigation dashboard

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

## ⚙ Installation

Clone the repository

git clone https://github.com/naveen-anon/cyber-portfolio.git  
cd cyber-portfolio

Install dependencies

pip install -r requirements.txt

---

## 🔑 Configuration

Edit config.py and add your API keys

SHODAN_API = "YOUR_SHODAN_API_KEY"  
OPENAI_API = "YOUR_OPENAI_API_KEY"  
SECRET_KEY = "matrix_osint_secret"

---

## ▶ Run the Project

python app.py

Open browser

http://127.0.0.1:5000

---

## 🧪 Usage

### Username Investigation

Enter a username and click Scan.

Example

naveen_anon

---

### Shodan Lookup

Enter an IP address.

Example

8.8.8.8

---

### Domain OSINT

Enter a domain name.

Example

example.com

---

### AI Investigation Report

Run any investigation and click Generate Report to create an AI-powered OSINT report.

---

## 🔌 API Endpoints

/username  → Sherlock username investigation  
/shodan    → Shodan host intelligence  
/domain    → Domain OSINT lookup  
/graph     → Investigation graph data  
/attacks   → Cyber attack map data  
/report    → AI investigation report  

---

## 🛠 Technologies Used

Python  
Flask  
Sherlock  
Shodan API  
OpenAI API  
JavaScript  
Matrix animation canvas  

---

## ⚠ Security Notice

Do not expose API keys publicly in GitHub repositories.

---

## 👨‍💻 Author

Naveen  
Cyber Security Enthusiast | OSINT Research  

GitHub  
https://github.com/naveen-anon
