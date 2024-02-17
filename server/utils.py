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

def new_book():
    title = input("Enter the title of the book  : ")
    author = input("Who wrote it?  :  ")
    price =input("How much is it?  :  ")
    book = Book(
        title = title,
        author = author,
        price = price,
    )
    db.session.add(book)
    db.session.commit()
    print(f"Book added successfully ..... {book.title}")















def add_book():
    book_titles = [book.title for book in db.session.query(Book).all()]
    prompt = input("Enter title of the Book  ->  ")
    book_title, index = pick(book_titles, prompt)
    title = db.session.query(Book).filter(Book.title == book_title).first()
    request_type = "Who is the author of this book?  ->  "
    author, index = pick(["Me","You","They","Them"],request_type)
    price_prompt = "How much is it?   "
    price = pick(["$12","$91","$10","$20"],price_prompt)
    date_str = input("Enter date and time book was written in the format YYYY-MM-DD HH:MM:SS ->   ")
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    book = Book(
        title = book_title,
        author = author,
        price = price,
        created_at = date
    )
    print("Book added successfully .....")
    db.session.add(book)
    db.session.commit()

