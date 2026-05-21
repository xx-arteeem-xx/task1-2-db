import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'library.db')

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    avatar_url = Column(String, nullable=True)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=True)
    price = Column(Float, nullable=True)
    author_id = Column(Integer, nullable=True)


engine = create_engine(f'sqlite:///{DB_PATH}')
Base.metadata.create_all(engine)
print("Таблица 'books' создана.")
