from src.database.db import SessionLocal
from src.models.user import User
from sqlalchemy.exc import IntegrityError
from src.services.auth_service import AuthService
import sys

def seed_users():
    users = [
        {
            "email": "admin@gmail.com",
            "password": "admin123",
        },
    ]

    try:
        with SessionLocal() as db:
            for user_data in users:
                existing_user = db.query(User).filter_by(email=user_data["email"]).first()
                if existing_user:
                    continue

                hashed_password = AuthService.hash_password(user_data["password"])
                user = User(email=user_data["email"], password=hashed_password)
                db.add(user)
            db.commit()
        print("Seeded users successfully!")
    except IntegrityError as e:
        print("Error seeding users:", e)
        sys.exit(1)

if __name__ == "__main__":
    seed_users()
