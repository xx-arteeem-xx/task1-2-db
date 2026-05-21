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

with Session(engine) as session:
    authors = [
        Author(name='Лев Толстой', country='Россия',
               avatar_url='https://example.com/tolstoy.jpg'),
        Author(name='Джордж Оруэлл', country='Великобритания',
               avatar_url='https://example.com/orwell.jpg'),
        Author(name='Марк Твен', country='США',
               avatar_url='https://example.com/twain.jpg'),
    ]
    session.add_all(authors)
    session.commit()

print("Три автора добавлены в базу данных.")
