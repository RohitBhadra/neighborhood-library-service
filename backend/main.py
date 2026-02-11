from fastapi import FastAPI, HTTPException
from .database import SessionLocal, engine, Base
from . import crud

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/books")
def create_book(title: str, author: str, published_year: int = None, isbn: str = None):
    db = SessionLocal()
    return crud.create_book(db, title, author, published_year, isbn)

@app.post("/members")
def create_member(name: str, email: str, phone: str = None, address: str = None):
    db = SessionLocal()
    return crud.create_member(db, name, email, phone, address)

@app.post("/borrow")
def borrow_book(book_id: int, member_id: int):
    db = SessionLocal()
    borrowing = crud.borrow_book(db, book_id, member_id)
    if not borrowing:
        raise HTTPException(status_code=400, detail="Book not available")
    return borrowing

@app.post("/return")
def return_book(borrowing_id: int):
    db = SessionLocal()
    borrowing = crud.return_book(db, borrowing_id)
    if not borrowing:
        raise HTTPException(status_code=400, detail="Invalid borrowing record")
    return borrowing

@app.get("/members/{member_id}/borrowings")
def list_borrowings(member_id: int):
    db = SessionLocal()
    return crud.list_borrowings_by_member(db, member_id)
