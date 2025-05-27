from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

# Config engine
engine = create_engine(
    "duckdb:///app.db",
    connect_args={
        'read_only': False,
        'config': {
            'memory_limit': '500mb'
        }
    }
)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    try:
        # Import model before creating tables
        from src.models.user import User

        # Create sequence for ID
        with engine.connect() as conn:
            conn.execute(text("CREATE SEQUENCE IF NOT EXISTS user_id_seq"))
            conn.commit()

            # Create tables by SQLAlchemy
            Base.metadata.create_all(bind=engine)

            # Check if tables are created
            tables = conn.execute(text("SELECT table_name FROM duckdb_tables")).fetchall()
            print("All tables in database:", tables)

    except Exception as e:
        print(f"Error initializing database: {e}")
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
