from sqlalchemy.orm import Session
from src.models.user import User
from hashlib import sha256

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        return sha256(password.encode()).hexdigest()

    @staticmethod
    def register_user(db: Session, email: str, password: str) -> bool:
        if not email or not password:
            raise Exception("Email and password are required")

        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise Exception("Email is already registered")

        hashed_password = AuthService.hash_password(password)
        new_user = User(email=email, password=hashed_password)

        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def login_user(db: Session, email: str, password: str) -> User:
        if not email or not password:
            raise Exception("Email and password are required")

        hashed_password = AuthService.hash_password(password)
        user = db.query(User).filter(
            User.email == email,
            User.password == hashed_password
        ).first()

        if user:
            return user

        raise Exception("Invalid email or password")
