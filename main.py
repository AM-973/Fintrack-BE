from dotenv import load_dotenv  
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.user import UserModel
from models.project import ProjectModel
from models.category import CategoryModel
from models.expense import ExpenseModel


from controllers.projects import router as ProjectsRouter
from controllers.categories import router as CategoriesRouter
from controllers.users import router as UsersRouter 
from controllers.expenses import router as ExpensesRouter

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://fintrack-p3f15hk6v-almatar973-gmailcoms-projects.vercel.app",
    "fintrack-fe-git-main-almatar973-gmailcoms-projects.vercel.app"
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Which sites can call this API
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],       # Allow all headers (e.g., Content-Type, Authorization)
    allow_credentials=True,
)


app.include_router(ProjectsRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")
app.include_router(CategoriesRouter, prefix="/api")
app.include_router(ExpensesRouter, prefix="/api")


@app.get("/")
def home():
    # Hello world function
    return "Welcome to FastAPI"

@app.get("/health")
def health_check():
    return {"ok": True}