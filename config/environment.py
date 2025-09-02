import os

if os.getenv("APP_ENV", "development") != "production":
    # load .env only locally
    from dotenv import load_dotenv
    load_dotenv()

DATABASE_URL = os.getenv("DB_URI")
db_URI = os.getenv("DB_URI")
secret = os.getenv("secret")

