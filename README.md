# bfhl-sql-automation
# 🧠 BFHL SQL Automation

A Python-based automation script that solves a SQL challenge and submits the solution using a generated webhook. Built as part of the BFHL (Bajaj Finserv Health Ltd) hiring task.

---

## 📌 Problem Summary

On application startup, the script:

1. Sends a POST request with user details to generate a **webhook URL** and an **access token**.
2. Solves a predefined **SQL problem** based on the registration number.
3. Submits the **final SQL query** automatically to the webhook using the token (no manual input or UI).

---

## 🛠 Tech Stack

- Python 3.x
- `requests` module
- RESTful APIs

---

## 🚀 How It Works

### 🔧 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SakshiIshwe0604/bfhl-sql-automation.git
   cd bfhl-sql-automation
