from  models import db,Book,Buyer
from pick import pick
from datetime import datetime

def get_all_buyers():
    return db.session.query(Buyer).all()


def exit_program():
    print("Goodbye!")
    exit()

def get_all_books():
    return db.session.query(Book).all()

def get_book_by_id(id):
    return db.session.get(Book,id)

def get_buyer_by_id(id):
    return db.session.get(Buyer,id)

def add_book():
    book_titles = [book.title for book in db.session.query(Book).all()]
    prompt = input("Enter title of the Book")
    book_title, index = pick(book_titles, prompt)
    title = db.session.query(Book).filter(Book.title == book_title).first()
    request_type = "Who is the author of this book?"
    author, index = pick(["Me","You","They","Them"],request_type)
    date_str = input("Enter date and time book was written in the format YYYY-MM-DD HH:MM:SS")
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
