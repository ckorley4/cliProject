from  models import db,Book,Buyer
from pick import pick
def get_all_buyers():
    return db.session.query(Buyer).all()


def get_all_books():
    return db.session.query(Book).all()

def get_book_by_id(id):
    return db.session.get(Book,id)

def get_buyer_by_id(id):
    return db.session.get(Buyer,id)

def add_book():
    title="Enter title of the Book"
    book_title,index=pick(title)
