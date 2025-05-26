from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import text
import duckdb

engine = create_engine("duckdb:///app.db")
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.clear()
    
    # Run migration: sau này có thể tách riêng ra script riêng, thư mục chứa sql riêng
    try:
        conn = duckdb.connect("app.db")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                email VARCHAR NOT NULL UNIQUE,
                password VARCHAR NOT NULL
            )
        """)
        conn.commit()
        
        tables = conn.execute("SELECT table_name FROM duckdb_tables").fetchall()
        print("All tables in database:", tables)
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
    
    # Cần thêm các model vào đây để có thể sử dụng ORM
    from src.models.user import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()