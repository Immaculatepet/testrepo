import csv
from collections import namedtuple

VW_Car = namedtuple("Car"," model year price transmission mileage fuelType tax mpg engineSize")

vw_cars = []

with open("vw.csv", "r", encoding="utf-8") as csvfile:
    print(csvfile)

    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    for row in reader:
        new_car = VW_Car(*row)
        vw_cars.append(new_car)
print(vw_cars)

# What is the most expensive vw car listed?

most_expensive_vw_car = []
expensive_vw_car = vw_cars[0]

for car in vw_cars:
    if int(car.price) > int(expensive_vw_car.price):
        expensive_vw_car = car
most_expensive_vw_car.append(expensive_vw_car)
print("\nTask 1:")
print("The most expensive vw car:")
print(most_expensive_vw_car)

# Find all the VW Golf models. WHat is their average price?
sum_of_vw_golf_models = 0
number_of_vw_cars = 0

for car in vw_cars:
    if car.model == "Golf":
        # check the sum total and number of VW Golf cars
        sum_of_vw_golf_models += int(car.price)
        number_of_vw_cars += 1
# Calculate the average price of the Golf cars 
avg_price_of_vw_golf = sum_of_vw_golf_models / number_of_vw_cars
print("\nTask 2:")
print(f"The average price of VW Golf cars is {round(avg_price_of_vw_golf)}")

# What is the average mileage for VW Polo models registered in 2020?

sum_of_2020_Polo_models = 0
number_of_2020_Polo_models = 0

for car in vw_cars:
    if car.model == "Polo" and int(car.year) == 2020:
        sum_of_2020_Polo_models += int(car.mileage)
        number_of_2020_Polo_models += 1
print(sum_of_2020_Polo_models)
print(number_of_2020_Polo_models)
avg_mileage = sum_of_2020_Polo_models / number_of_2020_Polo_models
print("\nTask 3:")
print(avg_mileage)
print(f"The average mileage of VW Polo models registered in 2020 is {round(avg_mileage)}")

used_vw_cars = []

for car in vw_cars:
    cars = VW_Car(
        car.model,
        car.year,
        car.price,
        car.transmission,
        car.mileage,
        car.fuelType,
        car.tax,
        car.mpg,
        car.engineSize
    )
    used_vw_cars.append(cars)
print(used_vw_cars)

with open("amend_vw.csv", "w") as new_csvfile:
    writer = csv.writer(new_csvfile,quoting=csv.QUOTE_ALL)
    writer.writerow(VW_Car\
                    ("Model","Year", "Price", "Transmission", "Mileage", "FuelType", "Tax","Mpg","EngineSize"))
    for car in used_vw_cars:
        writer.writerow(car)



