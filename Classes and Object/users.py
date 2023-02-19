# Make a class called User. 
# Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.

class User():
    """Class representing a user profile"""

    def __init__(self, first_name, last_name, username, email, gender, location):
        """Initialize user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.email = email
        self.gender = gender
        self.location = location.title()

    def describe_user(self):
        """The purpose of this function is to display a summary of user's profile"""
        print(f"Your first name: {self.first_name}")
        print(f"Your last name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location:{self.location}")
    
    def greet_user(self):
        """The purpose of this function is to greet the user"""
        print(f" Hello {self.username}!")


bara = User("Bara", "Kopackova", "justbaralol", "bara.kopackova@centrum.cz", "Female", "the czech republic" )
bara.describe_user()
bara.greet_user()

