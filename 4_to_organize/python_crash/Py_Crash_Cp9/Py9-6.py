# ICE CREAM STAND class
class Restaurant:
    """A model for a restaurant."""
    def __init__(self, restaurant_name, cuisine_type, number_served: int=0):
        """Initialize name and type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Print name and type"""
        print(f"The restaurant's name is {self.restaurant_name} and it is a(n) {self.cuisine_type} one."
              f"\nNumber of customers served: {self.number_served}")

    def open_restaurant(self):
        """Print a message saying that the local is open."""
        print(f"{self.restaurant_name} is open now!")

    def set_number_served(self, numbser_update: int):
        """It sets the number of customers served."""
        self.number_served = numbser_update

    def incre_number_served(self, add_number_served):
        """Increments the number of customers served."""
        self.number_served += add_number_served

class ice_cream_stand(Restaurant):
    """Models a Ice Cream Stand."""
    def __init__(self, restaurant_name, cuisine_name, number_served):
        """Initialize attributes of the Stand."""
        super().__init__(restaurant_name, cuisine_name, number_served)
        self.flavors = ['orange', 'banana', 'lemon']

    def display_flavors(self):
        """Displays available flavors."""
        print(f"The available flavors are:")
        for fi in self.flavors:
            print(f"\t- {fi}")

my_ice = ice_cream_stand('maldo', 'italian', 16)
my_ice.describe_restaurant()
my_ice.display_flavors()