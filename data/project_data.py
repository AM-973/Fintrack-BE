from models.project import ProjectModel

def create_test_projects():
    
    project1 = ProjectModel(
        project_name="Home Renovation",
        budget=50000,
        description="Complete kitchen and bathroom renovation project",
        user_id=1  # arjun_dev
    )
    
    project2 = ProjectModel(
        project_name="Wedding Planning",
        budget=25000,
        description="Planning and budgeting for wedding expenses",
        user_id=2  # emma_johnson
    )
    
    project3 = ProjectModel(
        project_name="Business Startup",
        budget=100000,
        description="Initial funding and expenses for new tech startup",
        user_id=1  # arjun_dev
    )
    
    project4 = ProjectModel(
        project_name="Vacation Fund",
        budget=8000,
        description="Saving and budgeting for European vacation",
        user_id=3  # fatima_ali
    )
    
    project5 = ProjectModel(
        project_name="Car Purchase",
        budget=30000,
        description="Budget for purchasing a new family car",
        user_id=4  # lucas_silva
    )
    
    project6 = ProjectModel(
        project_name="Emergency Fund",
        budget=20000,
        description="Building emergency savings fund",
        user_id=5  # elena_popov
    )

    return [project1, project2, project3, project4, project5, project6]

project_list = create_test_projects()
