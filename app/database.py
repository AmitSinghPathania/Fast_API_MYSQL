from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
# Update with your MySQL credentials: 'mysql+pymysql://user:password@host:port/db_name'
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@127.0.0.1:3306/enterprise_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_db_if_not_exists():
    # Connect to MySQL without specifying a database
    connection = pymysql.connect(host='127.0.0.1', user='root', password='')
    try:
        with connection.cursor() as cursor:
            # Create the DB only if it is missing
            cursor.execute("CREATE DATABASE IF NOT EXISTS enterprise_db")
        connection.commit()
    finally:
        connection.close()

# Run the check
create_db_if_not_exists()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def ensure_database_exists():
    connection = pymysql.connect(host='127.0.0.1', user='root', password='')
    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS enterprise_db")
        connection.commit()
    finally:
        connection.close()