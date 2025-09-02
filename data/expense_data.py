# data/expense_data.py

from models.expense import ExpenseModel

def create_test_expenses():
    
    # Expenses for Category 1: Kitchen (Project 1 - Home Renovation)
    expense1 = ExpenseModel(
        name="Kitchen Cabinets",
        amount=1500000,  # $15,000 in cents
        category_id=1
    )
    
    expense2 = ExpenseModel(
        name="Granite Countertops",
        amount=350000,  # $3,500 in cents
        category_id=1
    )
    
    expense3 = ExpenseModel(
        name="Kitchen Appliances",
        amount=280000,  # $2,800 in cents
        category_id=1
    )
    
    # Expenses for Category 2: Bathroom (Project 1 - Home Renovation)
    expense4 = ExpenseModel(
        name="Bathroom Tiles",
        amount=120000,  # $1,200 in cents
        category_id=2
    )
    
    expense5 = ExpenseModel(
        name="Toilet and Fixtures",
        amount=85000,  # $850 in cents
        category_id=2
    )
    
    # Expenses for Category 3: Venue (Project 2 - Wedding Planning)
    expense6 = ExpenseModel(
        name="Reception Hall Rental",
        amount=800000,  # $8,000 in cents
        category_id=3
    )
    
    expense7 = ExpenseModel(
        name="Ceremony Venue",
        amount=250000,  # $2,500 in cents
        category_id=3
    )
    
    # Expenses for Category 4: Catering (Project 2 - Wedding Planning)
    expense8 = ExpenseModel(
        name="Wedding Dinner",
        amount=450000,  # $4,500 in cents
        category_id=4
    )
    
    expense9 = ExpenseModel(
        name="Bar Service",
        amount=180000,  # $1,800 in cents
        category_id=4
    )
    
    # Expenses for Category 5: Photography (Project 2 - Wedding Planning)
    expense10 = ExpenseModel(
        name="Wedding Photographer",
        amount=200000,  # $2,000 in cents
        category_id=5
    )
    
    expense11 = ExpenseModel(
        name="Videography",
        amount=150000,  # $1,500 in cents
        category_id=5
    )
    
    # Expenses for Category 6: Equipment (Project 3 - Business Startup)
    expense12 = ExpenseModel(
        name="Laptops and Computers",
        amount=1200000,  # $12,000 in cents
        category_id=6
    )
    
    expense13 = ExpenseModel(
        name="Office Furniture",
        amount=450000,  # $4,500 in cents
        category_id=6
    )
    
    expense14 = ExpenseModel(
        name="Software Licenses",
        amount=320000,  # $3,200 in cents
        category_id=6
    )
    
    # Expenses for Category 7: Marketing (Project 3 - Business Startup)
    expense15 = ExpenseModel(
        name="Google Ads Campaign",
        amount=180000,  # $1,800 in cents
        category_id=7
    )
    
    expense16 = ExpenseModel(
        name="Social Media Marketing",
        amount=120000,  # $1,200 in cents
        category_id=7
    )
    
    expense17 = ExpenseModel(
        name="Website Development",
        amount=350000,  # $3,500 in cents
        category_id=7
    )
    
    # Expenses for Category 8: Legal (Project 3 - Business Startup)
    expense18 = ExpenseModel(
        name="Business Registration",
        amount=50000,  # $500 in cents
        category_id=8
    )
    
    expense19 = ExpenseModel(
        name="Legal Consultation",
        amount=280000,  # $2,800 in cents
        category_id=8
    )
    
    # Expenses for Category 9: Flights (Project 4 - Vacation Fund)
    expense20 = ExpenseModel(
        name="Round-trip Flights to Europe",
        amount=220000,  # $2,200 in cents
        category_id=9
    )
    
    # Expenses for Category 10: Accommodation (Project 4 - Vacation Fund)
    expense21 = ExpenseModel(
        name="Hotel in Paris",
        amount=120000,  # $1,200 in cents
        category_id=10
    )
    
    expense22 = ExpenseModel(
        name="Airbnb in Rome",
        amount=95000,  # $950 in cents
        category_id=10
    )
    
    # Expenses for Category 11: Activities (Project 4 - Vacation Fund)
    expense23 = ExpenseModel(
        name="Museum Tickets",
        amount=25000,  # $250 in cents
        category_id=11
    )
    
    expense24 = ExpenseModel(
        name="Food Tours",
        amount=18000,  # $180 in cents
        category_id=11
    )
    
    # Expenses for Category 12: Down Payment (Project 5 - Car Purchase)
    expense25 = ExpenseModel(
        name="Car Down Payment",
        amount=800000,  # $8,000 in cents
        category_id=12
    )
    
    # Expenses for Category 13: Insurance (Project 5 - Car Purchase)
    expense26 = ExpenseModel(
        name="Car Insurance Premium",
        amount=120000,  # $1,200 in cents
        category_id=13
    )
    
    # Expenses for Category 14: Medical Emergency (Project 6 - Emergency Fund)
    expense27 = ExpenseModel(
        name="Emergency Room Visit",
        amount=350000,  # $3,500 in cents
        category_id=14
    )
    
    expense28 = ExpenseModel(
        name="Prescription Medications",
        amount=85000,  # $850 in cents
        category_id=14
    )
    
    # Expenses for Category 15: Job Loss Buffer (Project 6 - Emergency Fund)
    expense29 = ExpenseModel(
        name="Monthly Living Expenses",
        amount=280000,  # $2,800 in cents
        category_id=15
    )
    
    expense30 = ExpenseModel(
        name="Utilities and Bills",
        amount=120000,  # $1,200 in cents
        category_id=15
    )

    return [expense1, expense2, expense3, expense4, expense5, expense6, expense7, 
            expense8, expense9, expense10, expense11, expense12, expense13, expense14,
            expense15, expense16, expense17, expense18, expense19, expense20, expense21,
            expense22, expense23, expense24, expense25, expense26, expense27, expense28,
            expense29, expense30]

expense_list = create_test_expenses()