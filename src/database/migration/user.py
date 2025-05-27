from sqlalchemy import text

def migrate(conn):
    tables = conn.execute("SELECT table_name FROM duckdb_tables").fetchall()
    if ('users',) not in tables:
        # Create sequence for ID
        conn.execute("CREATE SEQUENCE IF NOT EXISTS user_id_seq")

        # Create users table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                email VARCHAR NOT NULL UNIQUE,
                password VARCHAR NOT NULL
            )
        """)
        conn.commit()
        print("Created users table and user_id_seq sequence")
