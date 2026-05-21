import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'library.db')

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    avatar_url = Column(String, nullable=True)


engine = create_engine(f'sqlite:///{DB_PATH}')
Base.metadata.create_all(engine)
print("Таблица 'authors' создана.")
