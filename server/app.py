from config import app, migrate

from models import db
def home():
  print("Welcome to Our Book Store")

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    home()
    # remove pass and write your cli logic
