from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL =  DATABASE_URL = (
    "mssql+pyodbc://@ANDRIOD-PC\\SQLEXPRESS/fitnessDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

# def get_db():
#     db= SessionLocal()
#     try:
#         yield db
#     finally:db.close()


def test_db_connection():
    try:
        # Create a new session and test the connection
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("Database connection successful!")
    except Exception as e:
        print("Database connection failed:", e)
    finally:
        db.close()

# Run the test
test_db_connection()

# Dependency to get the database session
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
