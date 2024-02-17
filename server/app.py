from config import app, migrate

from models import db
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

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    home()
    while True:
      menu()
      break
    # remove pass and write your cli logic
