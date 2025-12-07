import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# For local development, we'll use SQLite
NEON_DATABASE_URL = os.getenv("NEON_DATABASE_URL", "postgresql://user:password@host:port/database")

engine = create_engine(NEON_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Database tables created (if they didn't exist).")

# Example for basic operation (optional for this foundational task, but useful)
def check_db_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print(f"Database connection successful. Result: {result.scalar()}")
    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    create_tables()
    check_db_connection()
