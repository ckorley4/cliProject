from config import app, migrate

from models import db
from utils import exit_program,get_all_books,update_book_title,get_all_buyers,update_book,new_book,delete_book,get_book_by_id,get_buyer_by_id
def home():
  print("Welcome to Our Book Store")

def menu():
  print("Please select an option:")
  print("0. Exit the program")
  print("1. List all Books")
  print("2. List all Buyers")
  print("3. Find book by isdn")
  print("4: Create Book")
  print("5: Update Book")
  print("6: Delete Book")
  print("7. Find buyer by card number")
  print("8: Create Buyer")
  print("9: Update Buyer")
  print("10: Delete Delete")

def display_all_buyers():
   buyers = get_all_buyers()
   for buyer in buyers:
      print(f"{buyer.id} --- {buyer.name}")

def display_all_books():
   books = get_all_books()
   for book in books:
      print(f"{book.isbn} -- {book.author}")

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    home()
    while True:
      menu()
      choice = input("> ")
      if choice == "0":
          exit_program()
      elif choice == "1":
          display_all_books()
      elif choice == "2":
          display_all_buyers()
      elif choice == "3":
         print("Hi")
           # find_department_by_id()
      elif choice == "4":
        new_book()
        print("Book added")
      elif choice == "5":
         book_isbn = input("Enter the isbn of book to rename : ")
         book = get_book_by_id(book_isbn)
         update_book_title(book)

      elif choice == "6":
         book_isbn = input("Enter the isbn of book to be deleted : ")
         book = get_book_by_id(book_isbn)
         if book:
            delete_book(book)
         else:
            print("There is no book with this ISBN")
      elif choice == "7":
         print("Hi")
            #list_employees()
      elif choice == "8":
         print("Hi")
           # find_employee_by_name()
      elif choice == "9":
         print("Hi")
           # find_employee_by_id()
      elif choice == "10":
         print("Hi")
           # create_employee()
      else:
            print("Invalid choice")
      
    # remove pass and write your cli logic
