animals = [
 {"name": "capybara", "group": "mammal", "weight": 110},
 {"name": "hedgehog", "group": "mammal", "weight": 0.5},
 {"name": "bearded dragon", "group": "reptile", "weight": 1},
 {"name": "tortoise", "group": "reptile", "weight": 40},
 {"name": "hummingbird", "group": "bird", "weight": 0.01},
 {"name": "elephant", "group": "mammal", "weight": 10000},
 {"name": "ostrich", "group": "bird", "weight": 280},
 {"name": "python", "group": "reptile", "weight": 180},
 {"name": "blue whale", "group": "mammal", "weight": 300000},
 {"name": "lion", "group": "mammal", "weight": 350}
]

# Let's consider the following tasks:
# 1. Print out all the animals names that are heavier than 100 pounds!
# loop through all the animal dicts inside the animals list
# check if the animal has a weight value of more than 100
# if it does, print out the name of the animal

for animal in animals:
    if(animal["weight"] > 100):
        print(animal["name"])

# 2. Print out the heaviest animal!
# loop through all the animal dicts inside the animals list
# Find out which animal has the highest weight value
# compare animals weights to each other
# once finished with all the animals, display the one with the highests weight.

heaviest_animal = animals[0]

for animal in animals:
    if(animal["weight"] > heaviest_animal["weight"]):
        heaviest_animal = animal

print(heaviest_animal)


# 3. Print out the lightest animal!

lightest_animal = animals[0]

for animal in animals:
    if(animal["weight"] < lightest_animal["weight"]):
        lightest_animal = animal

print(lightest_animal)

# 4. Print out all mammals as a list!

mammals = []

for animal in animals:
    if(animal["group"] == "mammal"):
        mammals.append(animal)

print(mammals)

# Print out a list of animals with longer names more than 7 letters

animals_with_long_names = []

for animal in animals:
    if( len(animal["name"]) > 7):
        animals_with_long_names.append(animal)

print(animals_with_long_names)