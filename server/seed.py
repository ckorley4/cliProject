from config import app
from models import db,Buyer,Book

from models import *

if __name__ == "__main__":
  with app.app_context():
    print ("Clearing out tables...")
    
    Book.query.delete()
    Buyer.query.delete()

    print("Seeding book table....")
   #new_book=input("Enter details of a book")
    #new_buyer=input('Enter a new buyer')
  
    new_book=Book(
      isbn="8989",
      author="Rooj",
      price="100"
    )
    db.session.add(new_book)
    db.session.commit()

   

    new_books=[
      Book(
      isbn="2323",
      author="Mants3 Takie",
      price="90",
      title="Claiming the Ga State",
    ),
    Book(
      isbn="1419",
      author="Rooja",
      price="12",
      title="Software Engineering for Guys",
    ),
    Book(
      isbn="7791",
      author="Lantz",
      price="150",
      title="Life Life",
    )
  
    ]
    db.session.add_all(new_books)
    db.session.commit()

    new_buyer=Buyer(
      name="Nii Korley",
      address="New York",
      book_isbn=new_book.isbn,
      card_number="123456"
    )
    db.session.add(new_buyer)
    db.session.commit()


    new_buyers=[
      Buyer(
      name="Nii",
      address="Harrison",
      book_isbn=new_books[2].isbn,
      card_number="678901"
    ),
    Buyer(
      name="Korley",
      address="New Haven",
      book_isbn=new_books[0].isbn,
      card_number="173756"
    ),
    Buyer(
      name="Anima",
      address="York City",
      book_isbn=new_books[2].isbn,
      card_number="4627"
    )
    ]
    
    db.session.add_all(new_buyers)
    db.session.commit()