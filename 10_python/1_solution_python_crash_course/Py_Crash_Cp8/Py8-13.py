# Program BUILD A PROFILE
def build_profile(first_name: str, last_name: str, **kwargs: str):
    """Build a user profile"""
    kwargs['first_name'] = first_name
    kwargs['last_name'] = last_name
    return kwargs

user_profile = build_profile('diego', 'diniz', local='sp', campo='stat')
print(user_profile)