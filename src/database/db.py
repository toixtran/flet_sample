from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Sequence
from src.database.base import Base
from sqlalchemy import inspect
from src.models import *

engine = create_engine("duckdb:///app.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_sequences_from_metadata():
    with engine.begin() as conn:
        for table in Base.metadata.tables.values():
            for column in table.columns:
                if hasattr(column.default, 'sequence'):
                    seq = column.default.sequence
                    if isinstance(seq, Sequence):
                        conn.execute(text(f"CREATE SEQUENCE IF NOT EXISTS {seq.name}"))

def sync_columns():
    with engine.begin() as conn:
        inspector = inspect(conn)

        for table in Base.metadata.tables.values():
            table_name = table.name
            model_columns = {col.name: col for col in table.columns}

            try:
                existing_columns_info = inspector.get_columns(table_name)
            except Exception:
                continue

            existing_columns = {col["name"] for col in existing_columns_info}

            for col_name, column in model_columns.items():
                if col_name not in existing_columns:
                    col_type = str(column.type.compile(engine.dialect))
                    default = f" DEFAULT {column.default.arg}" if column.default is not None and hasattr(column.default, "arg") else ""
                    nullable = "" if column.nullable else " NOT NULL"
                    alter_stmt = f"ALTER TABLE {table_name} ADD COLUMN {col_name} {col_type}{default}{nullable}"
                    try:
                        conn.execute(text(alter_stmt))
                        print(f"Added column '{col_name}' to '{table_name}'")
                    except Exception as e:
                        print(f"Failed to add column '{col_name}' to '{table_name}': {e}")

            for col in existing_columns:
                if col not in model_columns:
                    try:
                        conn.execute(text(f"ALTER TABLE {table_name} DROP COLUMN {col}"))
                        print(f"Dropped column '{col}' from '{table_name}'")
                    except Exception as e:
                        print(f"Failed to drop column '{col}' from '{table_name}': {e}")

def init_db():
    try:
        create_sequences_from_metadata()
        Base.metadata.create_all(bind=engine)
        sync_columns()

        with engine.connect() as conn:
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
