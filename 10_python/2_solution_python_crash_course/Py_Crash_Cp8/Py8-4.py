# Program Large shirt
def make_shirt(size: int = 30, mess: str = "I love python"):
    """Make a t-shirt with default values"""
    print(f"You made a T-shirt size {size}.")
    print(f"On that it's printed the message {mess}.")

make_shirt()
make_shirt(16)
make_shirt(mess="I don't love python")
make_shirt(16, "I don't love you")