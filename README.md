# 💰 FinTrack - Personal Finance Management Backend

[![Deployed on Heroku](https://img.shields.io/badge/Deployed%20on-Heroku-430098?style=for-the-badge&logo=heroku)](https://fintrack-77-46fcecc69fa7.herokuapp.com/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red?style=for-the-badge)](https://www.sqlalchemy.org/)

> **Your Complete Financial Planning Solution** 📊  
> Track expenses, manage budgets, and achieve your financial goals with intelligent planning algorithms and comprehensive project management.

## 📖 Table of Contents

- [✨ Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [🚀 Quick Start](#-quick-start)
- [🏗 Project Structure](#-project-structure)
- [📡 API Endpoints](#-api-endpoints)
- [💡 Financial Planning](#-financial-planning)

## ✨ Features

### 🎯 Core Functionality
- **📊 Project Management**: Create and manage financial projects with budget tracking
- **📂 Category Organization**: Organize expenses into customizable categories
- **💸 Expense Tracking**: Detailed expense management with real-time budget monitoring
- **👤 User Authentication**: Secure JWT-based authentication system
- **📈 Financial Planning**: Advanced algorithms for savings, investment, and hybrid plans
- **🔒 Data Security**: Complete user data isolation and ownership validation

### 🔧 Technical Features
- **🚀 RESTful API**: Fully RESTful endpoints following industry best practices
- **🏗️ Hierarchical Structure**: `Projects → Categories → Expenses` resource hierarchy
- **🔐 Secure Authentication**: JWT tokens with comprehensive authorization
- **📱 CORS Enabled**: Frontend-ready with proper cross-origin support
- **🗄️ PostgreSQL Database**: Robust relational database with migrations
- **⚡ High Performance**: Optimized queries and efficient data handling

## 🛠 Tech Stack

### Backend Infrastructure
```
🐍 Python 3.8+        - Programming language
⚡ FastAPI             - Modern web framework
🗄️ PostgreSQL         - Relational database
🔧 SQLAlchemy         - ORM and database toolkit
🔐 JWT                - Authentication tokens
🔒 bcrypt             - Password hashing
🌐 CORS               - Cross-origin resource sharing
📊 Pydantic           - Data validation and serialization
```

### Development Tools
```
📦 pipenv             - Dependency management
🔄 Alembic            - Database migrations
🧪 pytest            - Testing framework
🌍 uvicorn            - ASGI server
🔧 python-dotenv      - Environment variables
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database
- pipenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fintrack-backend.git
   cd fintrack-backend
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Environment setup**
   ```bash
   # Create .env file
   touch .env
   ```
   
   Add the following variables:
   ```env
   DB_URI=postgresql://username:password@localhost:XXXX/<db_name>
   secret=<JWT TOKEN SECRET>
   ```

4. **Database setup**
   ```bash
   # Run migrations
   alembic upgrade head
   
   # Seed the database (optional)
   python seed.py
   ```

5. **Start the development server**
   ```bash
   uvicorn main:app --reload 
   ```

🎉 **Server running at** `http://127.0.0.1:8000`

### API Documentation
- **Interactive Docs**: `http://127.0.0.1:8000/docs`

## 🏗 Project Structure

```
fintrack-backend/
├── 📁 controllers/              # API route handlers
│   ├── 👤 users.py             # User authentication & management
│   ├── 📊 projects.py          # Project CRUD operations
│   ├── 📂 categories.py        # Category management
│   └── 💸 expenses.py          # Expense tracking
├── 📁 models/                   # Database models
│   ├── 🏗️ base.py              # Base model with common fields
│   ├── 👤 user.py              # User model with auth
│   ├── 📊 project.py           # Project model with relationships
│   ├── 📂 category.py          # Category model
│   └── 💸 expense.py           # Expense model
├── 📁 serializers/              # Pydantic schemas
│   ├── 👤 user.py              # User validation schemas
│   ├── 📊 project.py           # Project schemas
│   ├── 📂 category.py          # Category schemas
│   └── 💸 expense.py           # Expense schemas
├── 📁 services/                 # Business logic
│   └── 📈 calculations.py      # Financial planning algorithms
├── 📁 dependencies/             # Shared dependencies
│   └── 🔐 get_current_user.py  # Authentication dependency
├── 📁 migrations/               # Database migrations
├── 📁 data/                     # Seed data
├── 📁 tests/                    # Test suites
├── 🔧 database.py              # Database configuration
├── 🚀 main.py                  # Application entry point
├── 🌱 seed.py                  # Database seeding
└── 📝 README.md                # Project documentation
```

## 📡 API Endpoints

### 🔐 Authentication
```http
POST   /api/register           # User registration
POST   /api/login              # User login
```

### 📊 Projects
```http
GET    /api/projects            # Get all user projects
GET    /api/projects/{id}       # Get specific project
POST   /api/projects            # Create new project
PUT    /api/projects/{id}       # Update project
DELETE /api/projects/{id}       # Delete project
```

### 📂 Categories (RESTful Hierarchy)
```http
GET    /api/projects/{project_id}/categories                    # Get project categories
GET    /api/projects/{project_id}/categories/{category_id}      # Get specific category
POST   /api/projects/{project_id}/categories                    # Create category
PUT    /api/projects/{project_id}/categories/{category_id}      # Update category
DELETE /api/projects/{project_id}/categories/{category_id}      # Delete category
```

### 💸 Expenses (RESTful Hierarchy)
```http
GET    /api/projects/{project_id}/categories/{category_id}/expenses                    # Get category expenses
GET    /api/projects/{project_id}/categories/{category_id}/expenses/{expense_id}      # Get specific expense
POST   /api/projects/{project_id}/categories/{category_id}/expenses                    # Create expense
PUT    /api/projects/{project_id}/categories/{category_id}/expenses/{expense_id}      # Update expense
DELETE /api/projects/{project_id}/categories/{category_id}/expenses/{expense_id}      # Delete expense
```

### 🔍 System
```http
GET    /                       # Welcome message
GET    /health                 # Health check
```

## 💡 Financial Planning

### 📈 Planning Algorithms

FinTrack includes sophisticated financial planning calculations:

#### 💰 Savings Plan
```python
# Calculates optimal saving strategy
{
  "monthly_saving": 1000,
  "total_saved": 6000,
  "months": 6
}
```

#### 📊 Investment Plan
```python
# Calculates investment growth with compound returns
{
  "monthly_contribution": 500,
  "total_value": 6152.50,
  "months": 12
}
```

#### 🔄 Hybrid Plan
```python
# Combines savings and investment strategies
{
  "savings_portion": 300,
  "investment_portion": 200,
  "total_plan_value": 5876.25
}
```

### 🎯 Plan Types
- **`savings`**: Conservative approach with guaranteed returns
- **`investment`**: Growth-focused with compound interest
- **`hybrid`**: Balanced approach combining both strategies

## 🔒 Security Features

- **🔐 JWT Authentication**: Secure token-based authentication
- **👤 User Isolation**: Complete data separation between users
- **🛡️ Authorization Checks**: Multi-level permission validation
- **🔒 Password Hashing**: bcrypt encryption for user passwords
- **🚫 CORS Protection**: Configured for specific frontend origins



## 🌍 Database

### 📊 Schema Overview
- **Users**: Authentication and profile management
- **Projects**: Financial projects with budget tracking
- **Categories**: Expense organization within projects
- **Expenses**: Individual expense tracking

### 🔄 Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

---

<div align="center">

### 💰 Built for Financial Success

**[📊 Frontend Repo](https://github.com/AM-973/fintrack-FE)** • **[⭐ Star this repo](https://github.com/AM-973/fintrack-BE)** 

Made by The Fintrack team | © 2025 FinTrack

</div>