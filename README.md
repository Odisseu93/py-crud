# PY CRUD

**Isekai title**: That Time I Created an API with [FastAPI](https://fastapi) and Python So I Wouldn´t Be Stuck with Just JavaScript.

> Attention: This repository was created solely for study purposes and has no intention of being useful in any way.

---

## Summary

[Installation](#installation)

## Installation

This project requires Python 3.8+ and uses a `requirements.txt` file to manage dependencies. Follow the steps below to set up your environment and install the necessary packages.

### 1. Set up a Virtual Environment (Recommended)

It is highly recommended to use a virtual environment to avoid conflicts with other global packages.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```

### 2. Install Dependencies

Once the virtual environment is active, run the following command to install all required libraries:

```bash
pip install -r requirements.txt

```

### Dependencies Overview

The project relies on the following core libraries:

- **FastAPI**: For building the web API.
- **Uvicorn**: An ASGI web server implementation for Python.
- **SQLAlchemy**: For database ORM mapping.
- **Pydantic**: For data validation and settings management.
- **Python-jose & Passlib**: For handling JWT authentication and password hashing.

| Package        | Version |
| -------------- | ------- |
| `fastapi`      | 0.128.0 |
| `uvicorn`      | 0.40.0  |
| `pydantic`     | 2.12.5  |
| `sqlalchemy`   | 2.0.46  |
| `cryptography` | 46.0.4  |

---

## Database

### Variables

```

```

### Diagram (DER)

```mermaid
---
title: PY CRUD
---
erDiagram

users {
   string id PK
   string name
   string email "UNIQUE"
   string password_hash
   boolean is_active
   boolean is_admin
   datetime created_at
   datetime updated_at
}

users ||--o{ orders : places

orders {
   string id PK
   string user_id FK
   string status "PENDING | CANCELED | COMPLETED"
   decimal total_price
   datetime created_at
   datetime updated_at
}

orders ||--o{ order_items : contains

products {
   string id PK
   string name
   string sku "UNIQUE"
   decimal price
   boolean is_active
}

products ||--o{ order_items : referenced_by

order_items {
   string id PK
   string order_id FK
   string product_id FK
   int quantity
   decimal unit_price
}

```

---
