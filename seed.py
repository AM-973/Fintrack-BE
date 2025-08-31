from sqlalchemy.orm import Session, sessionmaker
from config.environment import db_URI
from sqlalchemy import create_engine
from models.base import Base

# Import all models first to register them with SQLAlchemy
from models.user import UserModel
from models.project import ProjectModel  
from models.category import CategoryModel
from models.expense import ExpenseModel

from data.user_data import create_test_users
from data.project_data import create_test_projects
from data.category_data import create_test_categories

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding the database...")
    db = SessionLocal()

    # Create data lists after all models are loaded
    user_list = create_test_users()
    project_list = create_test_projects()
    category_list = create_test_categories()
 
    db.add_all(user_list)
    db.commit()
    
    db.add_all(project_list)
    db.commit()
    
    db.add_all(category_list)
    db.commit()

    

    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)
