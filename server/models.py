from config import db

class Book(db.Model):
    __tablename__='books'

    isbn=db.Column(db.Integer,primary_key=True)
    author=db.Column(db.String,unique=True)
    price=db.Column(db.Integer)
    sale_date=db.Column(db.DateTime, server_default=db.func.now())
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

class Buyer(db.Model):
    __tablename__='buyers'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String)
    book_isbn=db.Column(db.Integer, db.ForeignKey('books.isbn'))
    card_number=db.Column(db.Integer)
    purchase_date=db.Column(db.DateTime, server_default=db.func.now())
    