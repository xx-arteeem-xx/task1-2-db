import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

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

with Session(engine) as session:
    books = [
        Book(title='Война и мир', pages=1225, year=1869,
             rating=4.8, price=350.50, author_id=1),
        Book(title='Преступление и наказание', pages=500, year=1866,
             rating=4.7, price=270.00, author_id=1),
        Book(title='1984', pages=328, year=1949,
             rating=4.9, price=450.00, author_id=2),
    ]
    session.add_all(books)
    session.commit()

print("Три книги добавлены в базу данных.")
