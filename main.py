from dotenv import load_dotenv  
load_dotenv()
from fastapi import FastAPI
from controllers.projects import router as ProjectsRouter
from controllers.categories import router as CategoriesRouter
from controllers.users import router as UsersRouter 

app = FastAPI()

app.include_router(ProjectsRouter, prefix="/api",)
app.include_router(UsersRouter, prefix="/api")
app.include_router(CategoriesRouter, prefix="/api",)
# To add expense router *


@app.get("/")
def home():
    # Hello world function
    return "Welcome to FastAPI"