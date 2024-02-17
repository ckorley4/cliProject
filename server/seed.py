from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
    print ("Clearing out tables...")
    
    Book.query.delete()
    Buyer.query.delete()

  print("Seeding book table....")
  new_book=input("Enter details of a book")
  new_buyer=input('Enter a new buyer')

    

