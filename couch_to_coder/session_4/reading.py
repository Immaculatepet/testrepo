import csv
from collections import namedtuple

Book = namedtuple("Book", "name author user_rating reviews price year genre")
with open("bestsellers with categories.csv", "r", encoding='utf8') as csvfile:
 reader = csv.reader(csvfile, skipinitialspace=True)
 next(reader)

 books = [Book(*row) for row in reader]
#print(books)

## MINI-LAB

# Create a list with all of the bestsellers from 2009 to 2012!

filtered_bestsellers = []
for book in books:
    if(int(book.year) >= 2009 and int(book.year) <= 2012):
       filtered_bestsellers.append(book)
    #print(filtered_bestsellers)

# How expensive is the most expensive book?

most_expensive = books[0]
for book in books:
   if int(book.price) > int(most_expensive.price):
     most_expensive = book
#print(most_expensive)
# Create a list with all books whose author has the first name George!

george_books = []
for book in books:
   if("George" in book.author):
     george_books.append(book)
#print(george_books)

#writing to csv, modified price $1 = £0.79

#books = [Book(*row) for row in reader]

modified_books = []

for book in books:
   british_price_book = Book(
      book.name,
      book.author,
      book.user_rating,
      book.reviews,
      float(book.price)* 0.79,
      book.year,
      book.genre
   )
   modified_books.append(british_price_book)

#print(modified_books)

with open("bestsellers_british_price.csv", "w", encoding="utf8") as british_csvfile:
   writer = csv.writer(british_csvfile, quoting=csv.QUOTE_ALL)
   writer.writerow(Book("Name", "Author","User rating","Reviews","Price","Year","Genre"))
   for book in modified_books:
      writer.writerow(book)
