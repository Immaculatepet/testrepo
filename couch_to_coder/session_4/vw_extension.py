import pandas as pd
import matplotlib.pyplot as plt

# 1. A pie chart showing the distribution between fuel types
used_vw_cars = pd.read_csv("ammend_vw.csv")
#used_vw_cars = used_vw_cars.drop_duplicates(subset="Model",keep="last")

num_of_vw_cars_by_FuelType = used_vw_cars.groupby('FuelType')\
[['Model']].count().sort_values("Model", ascending=False).reset_index()
print("\nExtension 1:")
print("The FuelType are:")
print(num_of_vw_cars_by_FuelType)


plt.pie(
    num_of_vw_cars_by_FuelType.Model,
    labels=num_of_vw_cars_by_FuelType.FuelType,
    autopct="%1.1f%%")

plt.title("VW Cars Fuel Distrition")
plt.legend(title='FuelType:')
plt.show()

# 2. A bar chart showing the average mileage for each model.

model_type = used_vw_cars.groupby('Model')\
    [['Mileage']].mean().sort_values\
        ("Mileage", ascending=False).head(10).reset_index()

print("\nExtension 2:")
print("The Model Types are:")
print(round(model_type))

plt.bar(
    model_type.Model,
    model_type.Mileage,
    color = "Orange",
    width=0.5
)

plt.xlabel("VW Model")
plt.ylabel("Average Mileage")
plt.title("Distribution of Average Model against VW Model")
plt.xticks(rotation=45) # Rotate x-axis
plt.tight_layout()
plt.show()