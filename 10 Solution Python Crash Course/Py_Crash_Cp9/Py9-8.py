# A Class of USERS
class User:
    """A model of an user."""
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 age: int):
        """Initialize first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """Prints the user's information."""
        print(f"User information: {self.last_name}, {self.first_name}; {self.age} years old.")

    def greet_user(self):
        """Prints a message of a personalized greeting."""
        print(f"Hello {self.first_name}, welcome to our system!")

    def update_name(self,
                    updated_name):
        """Updates the user's name."""
        self.first_name = updated_name

class Privileges:
    """A set of privileges for the Admin Users."""
    def __init__(self):
        """Initialize atrributes."""
        self.privileges = ['can add post', 'can delete post']

    def show_privileges(self):
        """Shows the set of privileges."""
        print(f"The Admin privileges are:")
        for pi in self.privileges:
            print(f"\t- {pi.title()}.")

class Admin(User):
    """Models a Admin user."""
    def __init__(self,
                 first_name,
                 last_name,
                 age):
        """Initialize the attributes of the Admin."""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

new_admin = Admin('Diego', 'Diniz', 30)
new_admin.privileges.show_privileges()