# Class about a Restaurant
class Restaurant:
    """A model for a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print name and type"""
        print(f"The restaurant's name is {self.restaurant_name} and it is a(n) {self.cuisine_type} one.")

    def open_restaurant(self):
        """Print a message saying that the local is open."""
        print(f"{self.restaurant_name} is open now!")

my_rest = Restaurant('Raimundinho', 'Italian')
my_rest.describe_restaurant()
my_rest.open_restaurant()