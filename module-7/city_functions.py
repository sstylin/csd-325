
# Steve Stylin@Bellevue University
#Module 7.2 Test Cases

# city_functions.py


def city_country(city, country, population=None, language=None):
    """Return a formatted string of the form 'City, Country - population xxx, Language'."""
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    elif language:
        return f"{city}, {country}, {language}"
    else:
        return f"{city}, {country}"

# Function calls
print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France", 2148000))
print(city_country("Montreal", "Canada", 1780000, "French"))