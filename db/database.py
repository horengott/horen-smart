import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncResult
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DB_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DB_URL, echo=True)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()