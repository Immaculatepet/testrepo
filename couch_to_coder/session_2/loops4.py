students = [
    {"name": "Anna", "result": 92},
    {"name": "Colin", "result": 88},
    {"name": "Ed", "result": 98},
    {"name": "Joe", "result": 67}
]

total = 0

for student in students:
    total += student["result"]

mean_result = total / len(students)

print(mean_result)