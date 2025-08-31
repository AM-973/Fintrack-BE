import os
from sqlalchemy.orm import sessionmaker
from data.user_data import user_list
from sqlalchemy import create_engine
from models.base import Base
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

db_URI = os.getenv("db_URI")
if not db_URI:
    raise ValueError("db_URI not found in environment variables.")

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

def main():
    try:
        print("Recreating database...")
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        print("Seeding the database...")
        with SessionLocal() as db:
            db.add_all(user_list)
            db.commit()

        print("Database seeding complete! 👋")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()