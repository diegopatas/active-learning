# Program of City Names
def city_country(city: str, country: str):
    """Return a city name"""
    data_name = f"{city}, {country}."
    return data_name.title()

test = city_country("santiago", "chile")
print(test)