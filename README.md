# 💰 Finance Tracking Backend (FastAPI)

## 📌 Overview
This project is a Python-based finance tracking backend system built using FastAPI.  
It allows users to manage their financial records such as income and expenses, and provides useful summaries and analytics.

---

## 🚀 Features

- ➕ Add financial transactions (income/expense)
- 📄 View all transactions
- ✏️ Update transactions
- ❌ Delete transactions
- 🔍 Filter transactions by type or category
- 📊 Financial summary (total income, expense, balance)

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy

---

## 📂 Project Structure

finance_project/
│── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│── venv/
│── requirements.txt
│── README.md

---

## ▶️ How to Run

1. Clone the repository or download the project  
2. Open terminal inside project folder  
3. Activate virtual environment  

Windows:


terminal:-venv\Scripts\activate
pip install uvicorn
pip list
unicorn app.main:app --reload