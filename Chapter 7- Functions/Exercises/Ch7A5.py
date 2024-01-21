def describe_city(city, country='America'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('New York')
describe_city('Davao', 'Philippines')
describe_city('Los Angeles')