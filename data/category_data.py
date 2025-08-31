# data/category_data.py

from models.category import CategoryModel

def create_test_categories():
    # Categories for project 1 (Home Renovation)
    category1 = CategoryModel(
        name="Kitchen",
        budget=30000,
        description="Kitchen renovation expenses",
        project_id=1
    )
    
    category2 = CategoryModel(
        name="Bathroom",
        budget=20000,
        description="Bathroom renovation expenses", 
        project_id=1
    )
    
    # Categories for project 2 (Wedding Planning)
    category3 = CategoryModel(
        name="Venue",
        budget=12000,
        description="Wedding venue and reception costs",
        project_id=2
    )
    
    category4 = CategoryModel(
        name="Catering",
        budget=8000,
        description="Food and beverage expenses",
        project_id=2
    )
    
    category5 = CategoryModel(
        name="Photography",
        budget=3000,
        description="Wedding photography and videography",
        project_id=2
    )
    
    # Categories for project 3 (Business Startup)
    category6 = CategoryModel(
        name="Equipment",
        budget=40000,
        description="Computer hardware and office equipment",
        project_id=3
    )
    
    category7 = CategoryModel(
        name="Marketing",
        budget=25000,
        description="Digital marketing and advertising",
        project_id=3
    )
    
    category8 = CategoryModel(
        name="Legal",
        budget=15000,
        description="Legal fees and business registration",
        project_id=3
    )
    
    # Categories for project 4 (Vacation Fund)
    category9 = CategoryModel(
        name="Flights",
        budget=3000,
        description="Airline tickets for European vacation",
        project_id=4
    )
    
    category10 = CategoryModel(
        name="Accommodation",
        budget=2500,
        description="Hotels and lodging expenses",
        project_id=4
    )
    
    category11 = CategoryModel(
        name="Activities",
        budget=1500,
        description="Tours, museums, and entertainment",
        project_id=4
    )
    
    # Categories for project 5 (Car Purchase)
    category12 = CategoryModel(
        name="Down Payment",
        budget=10000,
        description="Initial down payment for car",
        project_id=5
    )
    
    category13 = CategoryModel(
        name="Insurance",
        budget=2000,
        description="Car insurance premiums",
        project_id=5
    )
    
    # Categories for project 6 (Emergency Fund)
    category14 = CategoryModel(
        name="Medical Emergency",
        budget=10000,
        description="Healthcare and medical expenses",
        project_id=6
    )
    
    category15 = CategoryModel(
        name="Job Loss Buffer",
        budget=10000,
        description="Income replacement fund",
        project_id=6
    )

    return [category1, category2, category3, category4, category5, category6, 
            category7, category8, category9, category10, category11, category12,
            category13, category14, category15]

category_list = create_test_categories()
