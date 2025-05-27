## Demo Desktop App
A simple desktop application built with Python Flet, DuckDB, and SQLAlchemy.
Features

User registration
User login
Dashboard
Navbar-based navigation

## Requirements

Python 3.8+
See requirements.txt for dependencies

## Setup

Clone the repository
Create a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install dependencies:

```sh
pip install -r requirements.txt
```

## Run the application:

```sh
python main.py
```

## Project Structure

```
python-flet/
├── README.md
├── requirements.txt
├── db.py                  # CLI commands for database
├── main.py               # Entry point
├── src/
│   ├── __init__.py
│   ├── models/           # Database models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/         # Business logic
│   │   ├── __init__.py
│   │   └── auth_service.py
│   ├── ui/              # UI components
│   │   ├── __init__.py
│   │   ├── layout.py
│   │   ├── components/
│   │   │   ├── __init__.py
│   │   │   └── navbar.py
│   │   └── screens/    # Screen
│   │       ├── __init__.py
│   │       ├── login.py
│   │       ├── register.py
│   │       └── dashboard.py
│   └── database/        # Database configuration
│       ├── __init__.py
│       ├── db.py        # Database connection
│       └── seeder/      # Database seeders
│           ├── __init__.py
│           ├── base_seeder.py
│           └── user_seeder.py
└── app.db               # Database file
```

### Database CLI
Database :
```sh
    python db.py --help
```
