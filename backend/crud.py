from sqlalchemy.orm import Session
from . import models
import datetime

# BOOK CRUD
def create_book(db: Session, title: str, author: str, published_year: int = None, isbn: str = None):
    book = models.Book(title=title, author=author, published_year=published_year, isbn=isbn)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def list_books(db: Session):
    return db.query(models.Book).all()

# MEMBER CRUD
def create_member(db: Session, name: str, email: str, phone: str = None, address: str = None):
    member = models.Member(name=name, email=email, phone=phone, address=address)
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.id == member_id).first()

def list_members(db: Session):
    return db.query(models.Member).all()

# BORROWING CRUD
def borrow_book(db: Session, book_id: int, member_id: int, due_date: datetime.datetime = None):
    book = get_book(db, book_id)
    if not book or not book.available:
        return None
    borrowing = models.Borrowing(book_id=book_id, member_id=member_id, due_date=due_date)
    book.available = False
    db.add(borrowing)
    db.commit()
    db.refresh(borrowing)
    return borrowing

def return_book(db: Session, borrowing_id: int):
    borrowing = db.query(models.Borrowing).filter(models.Borrowing.id == borrowing_id).first()
    if not borrowing or borrowing.returned_at:
        return None
    borrowing.returned_at = datetime.datetime.utcnow()
    book = get_book(db, borrowing.book_id)
    book.available = True
    db.commit()
    db.refresh(borrowing)
    return borrowing

def list_borrowings_by_member(db: Session, member_id: int):
    return db.query(models.Borrowing).filter(models.Borrowing.member_id == member_id).all()
