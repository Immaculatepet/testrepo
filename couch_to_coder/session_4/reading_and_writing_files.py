import csv
import pandas as pd
import matplotlib.pyplot as plt

from collections import namedtuple

Book = namedtuple("Book","name author user_rating reviews price year genre")

books = []

with open("bestsellers with categories.csv", "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    for row in reader:
        #print(row)

        # new_book = {}
        # new_book["name"] = row[0]
        # new_book["Author"] = row[1]
        # new_book["User Rating"] = row[2]
        # new_book["Reviews"] = row[3]
        # new_book["Price"] = row[4]
        # new_book["Year"] = row[5]
        # new_book["Genre"] = row[6]
        # books.append(new_book)
        #new_book = Book(row[0],row[1], row[2],row[3],row[4],row[5],row[6])
        new_book = Book(*row)
        books.append(new_book)
    #print(books[0])

    
# Create a list with all of the bestsellers from 2009 to 2012!
# filtered_bestsellers =[]

# for book in books:
#     if int(book.year) >=2009 and int(book.year) <= 2012:
#         filtered_bestsellers.append(book)

filtered_bestseller = [book for book in books if int(book.year) >=2009 and int(book.year) <= 2012]
print(filtered_bestseller)



#How expensive is the most expensive book?
#Create a list with all books whose author has the first name George!