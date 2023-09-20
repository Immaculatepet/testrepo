import pandas as pd
import matplotlib.pyplot as plt

bestsellers = pd.read_csv("bestsellers with categories.csv")
bestsellers = bestsellers.drop_duplicates(subset="Name",keep="last")
#print(bestsellers)

# 1. Create a bar chart showing the author with the most amount of bestselling titles in the
# given years.

number_of_books_written = bestsellers.groupby('Author')\
[['Name']].count().sort_values("Name", ascending=False).head(10).reset_index()

#print(number_of_books_written)
# plt.bar(number_of_books_written.Author,
#  number_of_books_written.Name,
#  color ='maroon',
#  width = 0.4)
# plt.xlabel("Authors")
# plt.ylabel("Number of bestselling books")
# plt.title("Number of bestselling books by author")
#plt.show()

# 2. Create a pie chart showing the distribution between fiction and non-fiction books!

number_of_books_by_genre = bestsellers.groupby('Genre')\
    [['Name']].count().sort_values("Name", ascending=False).reset_index()

plt.pie(number_of_books_by_genre.Name, 
        labels=number_of_books_by_genre.Genre, 
        autopct="%1f%%")
plt.show()