# Task
# create a List for the logest rivers in the world!

rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

# Task 1. In a for loop, print out each river's name!

for river in rivers:
   
    print( river["name"])

# Task 2. Calculate and print out the total length of all the rivers!

total_length = 0
   
for river in rivers:
    total_length += river["length"]

print("\nTask 2:")
print("Total length of all the rivers:", total_length, "miles")

# Extensions 

# 1: Print rivers whose names begins with 'M'!
print("\nExtension 1:")
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])

# Extensions 2: Convert and print river's length in kilometers
print("\nExtension 2:")

for river in rivers:
    length_km = river["length"] * 1.6
    print(f"{river['name']} - Length: {length_km:.2f} km")