from sqlalchemy.orm import Session
from sqlalchemy import text
from src.models.user import User
from hashlib import sha256

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        return sha256(password.encode()).hexdigest()

    @staticmethod
    def register_user(db: Session, email: str, password: str) -> bool:
        try:
            # Check if user exists
            if db.query(User).filter(User.email == email).first():
                return False

            # Create new user
            hashed_password = AuthService.hash_password(password)
            new_user = User(email=email, password=hashed_password)
            db.add(new_user)
            db.commit()
            return True
        except Exception as e:
            print(f"Error registering user: {e}")
            db.rollback()
            return False

    @staticmethod
    def login_user(db: Session, email: str, password: str) -> bool:
        hashed_password = AuthService.hash_password(password)
        user = db.query(User).filter(
            User.email == email,
            User.password == hashed_password
        ).first()
        return bool(user)
