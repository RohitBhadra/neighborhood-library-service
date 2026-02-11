from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from .database import Base
import datetime

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer)
    isbn = Column(String, unique=True)
    available = Column(Boolean, default=True)

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(String)

class Borrowing(Base):
    __tablename__ = "borrowings"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    borrowed_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    due_date = Column(TIMESTAMP)
    returned_at = Column(TIMESTAMP, nullable=True)
