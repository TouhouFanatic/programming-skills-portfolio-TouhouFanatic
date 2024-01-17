rivers = {
    'Nile': 'Egypt',
    'Yangtze': 'South America',
    'Amazon': 'Amazon',
    'Mississippi': 'North America',
    'Ganges': 'India',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nListed Rivers:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nListed Countries:")
for country in rivers.values():
    print(f"- {country.title()}")