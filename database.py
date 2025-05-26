
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Ensure these environment variables are set in your .env file
DB_USER = os.getenv("MYSQL_USER", "root")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_PORT = os.getenv("MYSQL_PORT", "3306")
DB_NAME = os.getenv("MYSQL_DATABASE", "jobs")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" # Changed to pymysql for easier installation

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
