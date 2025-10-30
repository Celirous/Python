print('\n') 

# ============================================ 
        # Class AdminPrivileges:
# ============================================ 

class AdminPrivileges:
    """A simple class to store admin privileges"""

    def __init__(self, privileges=None):
        """This stores the priviliges"""
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        """This will show your profile access"""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# ============================================ 
        # Class GuestPrivileges:
# ============================================ 

class GuestPrivileges:
    """A simple class to store admin privileges"""

    def __init__(self, privileges=None):
        """This stores the priviliges"""
        if privileges is None:
            privileges = ["can view post", "can comment on post"]
        self.privileges = privileges

    def show_privileges(self):
        """This will show your profile access"""
        print("Guest privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# ============================================ 
        # Class User:
# ============================================ 

class User: 

    #Constuctor 
    def __init__(self, first_name, last_name, email):#,user_access):
        """This is to create a User Profile"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # self.user_access = user_access
        self.login_attempts = 0

    #Methods and attributes 

    def describe_user(self):
        """This is all user info"""
        return f"{self.first_name.title()}, {self.last_name.title()}, {self.email}"
        
    
    def greet_user(self):
        """Generating a greeting for the user"""
        return f'Hey there {self.first_name.title()}, welcome to our system.'

    def increment_login_attempts(self):
        """This will increment your login attempts by 1"""
        self.login_attempts += 1
        

    def reset_login_attempts(self):
        """This will generate how many times you have tried to login"""
        self.login_attempts = 0
        
    # def show_privileges(self):
    #     """This will show your profile access"""
    #     return f'{self.first_name} your user access is set to: {self.user_access.title()}'


# ============================================ 
        # Sub Class Admin Class:
# ============================================

class Admin(User):
    """Admin is a special type of user with privileges"""

    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = AdminPrivileges()



# ============================================ 
        # Sub Class Guest Class:
# ============================================

class Guest(User):
    """This is a view only profile, Guest Profile"""

    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = GuestPrivileges()










# ============================================
# Create Users
# ============================================
admin_1 = Admin("A.J.", "Bellringer", "aj.bellringer@gmail.com")
guest_1 = Guest("Sam", "Peterson", "sam.peterson@example.com")
user_1 = User("Riley", "Williams", "riley.williams@example.com")


# ============================================
# Display Users
# ============================================
print(admin_1.describe_user())
print(admin_1.greet_user())
print('\n') 
print(guest_1.describe_user())
print(guest_1.greet_user())
print('\n')
print(user_1.describe_user())
print(user_1.greet_user())
print('\n')


# ============================================
# Test Login Attempts
# ============================================

admin_1.increment_login_attempts()
admin_1.increment_login_attempts()
admin_1.increment_login_attempts()
print(f"Login attempts for {admin_1.first_name}: {admin_1.login_attempts}")


admin_1.reset_login_attempts()
print(f"Login attempts after reset for {admin_1.first_name}: {admin_1.login_attempts}")
print('\n')


# ============================================
# Show Privileges
# ============================================

admin_1.privileges.show_privileges()
print('\n') 
guest_1.privileges.show_privileges()
print('\n')