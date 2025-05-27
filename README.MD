Demo Desktop App
A simple desktop application built with Python Flet, DuckDB, and SQLAlchemy.
Features

User registration
User login
Dashboard
Navbar-based navigation

Requirements

Python 3.8+
See requirements.txt for dependencies

Setup

Clone the repository
Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the application:

python main.py

Run migration

python src/database/migration.py

Project Structure

src/models/: Database models
src/services/: Business logic
src/ui/: UI components and screens
src/database/: Database configuration
main.py: Application entry point

