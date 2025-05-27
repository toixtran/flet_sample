from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.database.migration.user import migrate as migrate_user
import duckdb

engine = create_engine("duckdb:///app.db")
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.clear()
    try:
        conn = duckdb.connect("app.db")
        migrate_user(conn)

        tables = conn.execute("SELECT table_name FROM duckdb_tables").fetchall()
        print("All tables in database:", tables)

        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise

    # Cần thêm các model vào đây để có thể sử dụng ORM
    from src.models.user import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
