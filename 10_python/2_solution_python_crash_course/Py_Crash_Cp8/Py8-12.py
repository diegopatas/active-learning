# Program Sandwiches
def make_sandwich(*order: str):
    """Prints an order of sandwiches."""
    print(" You have ordered the following sandwiches:")
    print(order)

make_sandwich('egg')
make_sandwich('egg', 'bacon')
make_sandwich('egg', 'bacon', 'salad')
