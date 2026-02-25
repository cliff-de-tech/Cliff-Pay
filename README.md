<div align="center">

# 💳 Cliff-Pay

### A Secure Digital Wallet & Peer-to-Peer Transfer API

*Built for reliability. Engineered for integrity.*

---

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-red?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/SimpleJWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

</div>

---

## 📖 About

**Cliff-Pay** is a production-grade backend API for a digital wallet system with peer-to-peer fund transfer capabilities. Built with Django and Django REST Framework, it demonstrates real-world backend engineering patterns including atomic database transactions, signal-driven architecture, and token-based authentication — all designed to handle financial data with precision and security.

> 🎓 **Capstone Project** — Engineered by a Backend Developer & Creative Technologist.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 **Custom User Model** | Email-based authentication replaces the default Django username model, providing a cleaner and more modern auth flow. |
| 👛 **Automated Wallet Generation** | Every new user automatically receives a wallet upon registration, powered by **Django Signals** (`post_save`). Zero manual setup required. |
| 💸 **Secure P2P Transfers** | Fund transfers between wallets are wrapped in `transaction.atomic()`, guaranteeing **database integrity** — if any step fails, the entire operation rolls back. No funds are ever lost or duplicated. |
| 🛡️ **JWT Authentication** | All protected endpoints are secured with **SimpleJWT** access/refresh tokens, ensuring stateless and scalable authentication. |
| 📒 **Transaction Ledger** | Full history of all sent and received transfers, queryable per user for complete financial transparency. |

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| Framework | Django 4.x |
| API Layer | Django REST Framework |
| Database | PostgreSQL |
| Authentication | djangorestframework-simplejwt |

---

## 🚀 Local Setup & Installation

### Prerequisites

- Python 3.11+
- PostgreSQL installed and running
- `pip` and `virtualenv`

### 1. Clone the Repository

```bash
git clone https://github.com/cliff-de-tech/Cliff-Pay.git
cd Cliff-Pay
```

### 2. Create & Activate a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/cliffpay_db
```

> ⚠️ **Never commit your `.env` file.** Ensure it is listed in `.gitignore`.

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## 📡 API Endpoints Reference

All protected routes require an `Authorization: Bearer <access_token>` header.

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `POST` | `/api/accounts/register/` | Register a new user (wallet auto-created) | ❌ No |
| `POST` | `/api/accounts/login/` | Obtain JWT access & refresh tokens | ❌ No |
| `GET` | `/api/accounts/profile/` | View authenticated user profile & wallet balance | ✅ Yes |
| `POST` | `/api/transactions/send/` | Transfer funds to another user's wallet | ✅ Yes |
| `GET` | `/api/transactions/history/` | View full transaction ledger (sent & received) | ✅ Yes |

### 📋 Example Requests

<details>
<summary><strong>Register a New User</strong></summary>

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "cliff",
    "password": "securepassword123"
  }'
```

</details>

<details>
<summary><strong>Login (Obtain Tokens)</strong></summary>

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

</details>

<details>
<summary><strong>Send Funds (P2P Transfer)</strong></summary>

```bash
curl -X POST http://127.0.0.1:8000/api/transactions/send/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access_token>" \
  -d '{
    "recipient": "recipient@example.com",
    "amount": "50.00"
  }'
```

</details>

---

## 🧠 Architecture Highlights

```
cliff-pay/
├── accounts/          # Custom user model, wallet, auth endpoints
│   ├── models.py      # User + Wallet models
│   ├── signals.py     # post_save → auto wallet creation
│   ├── serializers.py # Registration & profile serializers
│   └── views.py       # Register, login, profile views
├── transactions/      # P2P transfer logic
│   ├── models.py      # Transaction model (sender, receiver, amount)
│   ├── views.py       # Atomic transfer & history views
│   └── serializers.py # Transfer & history serializers
├── core/              # Django project settings & root URL config
└── manage.py
```

---

## 👤 Author

**Clifford Opoku-Sarkodie** — *Backend Engineer & Creative Technologist*

🔗 GitHub: [@cliff-de-tech](https://github.com/cliff-de-tech)

---

<div align="center">

*Built with 🖤 and Python.*

</div>
