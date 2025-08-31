from dotenv import load_dotenv  
load_dotenv()
from fastapi import FastAPI

from models.user import UserModel
from models.project import ProjectModel
from models.category import CategoryModel
from models.expense import ExpenseModel


from controllers.projects import router as ProjectsRouter
from controllers.categories import router as CategoriesRouter
from controllers.users import router as UsersRouter 
from controllers.expenses import router as ExpensesRouter

app = FastAPI()

app.include_router(ProjectsRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")
app.include_router(CategoriesRouter, prefix="/api")
app.include_router(ExpensesRouter, prefix="/api")


@app.get("/")
def home():
    # Hello world function
    return "Welcome to FastAPI"