pets = []
pet = {
    'Owner': 'Akisha',
    'Name': 'Cowsy',
    'Animal': 'Cat',
    'Age': 'Dead',
    'Hobby': 'Being in a jar, being ash',
}
pets.append(pet)

pet = {
    'Owner': 'Jed',
    'Name': 'Churo',
    'Animal': 'Dog',
    'Age': 9,
    'Hobby': """Peeing in places they shouldn't""",
}
pets.append(pet)

pet = {
    'Owner': 'Jaiden',
    'Name': 'Ari',
    'Animal': 'Parrot',
    'Age': 5,
    'Hobby': 'Squaking',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['Owner'].title()}'s pet:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")