from config import db

class Book(db.Model):
    __tablename__='books'

    isbn=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    author=db.Column(db.String,unique=True)
    price=db.Column(db.Integer)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"Title: {self.title} Author: {self.author}"

class Buyer(db.Model):
    __tablename__='buyers'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String)
    book_isbn=db.Column(db.Integer, db.ForeignKey('books.isbn'))
    card_number=db.Column(db.Integer)
    purchase_date=db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr_(self):
        return f"Name: {self.name} Card_number: {self.card_number}"