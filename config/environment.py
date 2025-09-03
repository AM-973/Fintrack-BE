import os

if os.getenv("APP_ENV", "development") != "production":
    # load .env only locally
    from dotenv import load_dotenv
    load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("DB_URI")

# Handle Heroku's postgres:// URL format (needs to be postgresql://)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

db_URI = DATABASE_URL
secret = os.getenv("secret")

