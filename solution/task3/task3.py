import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

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


def print_authors():
    with Session(engine) as session:
        authors = session.query(Author).all()
        for author in authors:
            print(f'Имя: {author.name}, Страна: {author.country}')


print_authors()
