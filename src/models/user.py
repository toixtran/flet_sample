from sqlalchemy import Column, Integer, String, Sequence, DateTime, Boolean
from sqlalchemy.sql import func
from src.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        Sequence("user_id_seq"),
        primary_key=True,
        server_default=Sequence("user_id_seq").next_value()
    )
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=True)
    created_by = Column(String, nullable=True)
    updated_by = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
