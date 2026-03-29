from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Settings as settings

SQLALCHEMY_DATABASE_URL = f'postgresql://jdeeza:password123@localhost:5432/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        

# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost',
#                                 database = 'fastapi',
#                                 user = 'postgres',
#                                 password = 'password123',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connected")
#         break
#     except Exception as error:
#         print(error)
#         time.sleep(2)