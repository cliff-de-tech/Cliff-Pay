# Cliff-Pay 💳
A secure, Peer-to-Peer (P2P) digital wallet API built with Django and PostgreSQL.

## 🚀 Features
- **Secure Authentication:** Custom User model with JWT support.
- **Smart Wallets:** Automatic wallet creation upon registration.
- **Security First:** Built-in `daily_limit` checks for all transactions.
- **Atomic Transactions:** Ensures money is never lost during transfers.

## 🛠️ Tech Stack
- **Backend:** Django REST Framework (Python)
- **Database:** PostgreSQL
- **Security:** Django Signals & Environment Variables

## 📦 Setup
1. Clone the repo.
2. Run `pip install -r requirements.txt`.
3. Set up your `.env` file.
4. Run `python manage.py migrate`.