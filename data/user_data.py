from models.user import UserModel

def create_test_users():
    # Regular users
    user1 = UserModel(username="arjun_dev", email="arjun@devmail.in", is_admin=False)
    user1.set_password("securepassword1")
    
    user2 = UserModel(username="emma_johnson", email="emma.johnson@email.com", is_admin=False)
    user2.set_password("securepassword2")
    
    user3 = UserModel(username="fatima_ali", email="fatima.ali@mail.ae", is_admin=False)
    user3.set_password("securepassword3")
    
    user4 = UserModel(username="lucas_silva", email="lucas.silva@correo.br", is_admin=False)
    user4.set_password("securepassword4")
    
    user5 = UserModel(username="elena_popov", email="elena.popov@mail.ru", is_admin=False)
    user5.set_password("securepassword5")
    
    # Admin users for testing
    admin1 = UserModel(username="admin", email="admin@fintrack.com", is_admin=True)
    admin1.set_password("admin123")
    
    admin2 = UserModel(username="super_admin", email="superadmin@fintrack.com", is_admin=True)
    admin2.set_password("superadmin123")
    
    admin3 = UserModel(username="test_admin", email="testadmin@fintrack.com", is_admin=True)
    admin3.set_password("testadmin123")
    
    string_admin = UserModel(username="string", email="string@test.com", is_admin=True)
    string_admin.set_password("string")

    return [user1, user2, user3, user4, user5, admin1, admin2, admin3, string_admin]

user_list = create_test_users()