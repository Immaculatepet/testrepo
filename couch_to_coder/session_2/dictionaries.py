student ={
    "first_name": "Anna",
    "last_name": "Henderson",
    "subject": "chemistry",
    "result": 92,
    "contact_details": {
        "phone": "+447464150571",
        "email": "anna@exmaple.com"
    }
    }

student["date_of_birth"] = "1990/01/01"
# print(student["first_name"])
# print(student["contact_details"])
# print(student["date_of_birth"])
# print("first_name" in student)

# print( student.keys())
# print( student.values())

# get the phone number printed out only
print( student["contact_details"]["phone"] )