# A Class of USERS
class User:
    """A model of an user."""

    def __init__(self, first_name: str, last_name: str, age: int):
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

    def update_name(self, updated_name):
        """Updates the user's name."""
        self.first_name = updated_name

user_01 = User('Diego', 'Diniz', 19)
user_02 = User('Mario', 'Morais', 33)
user_01.first_name = 'oswaldo'
user_01.update_name('Diresgo')
user_01.describe_user()
user_01.greet_user()
user_02.describe_user()
user_02.greet_user()