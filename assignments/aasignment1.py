#Create a list of your favorite movies and print it. Then, append a new movie to the list and
#print the updated list.

movies = ["spiderman","Thor","ironman","peaky blinders"]
print(movies)
movies.append("captain america")
print(movies)

# Create a list of integers from 1 to 10 and print it. Calculate the sum of all the numbers in
# the list and print the result. 

integers = [1,2,3,4,5,6,7,8,9,10]
sum = 0 ; 
for i in integers:
    print(i)
    sum = sum + i;
print(sum)

# Create a list of mixed data types including strings, integers, and floats and print it. Remove
# the first element from the list and print the modified list.

mixed = ["Name" , 7 , 7.77]
for i in mixed:
    print(type(i))

# Create a tuple containing the names of the days of the week and print it. Access and print
# the name of the third day.

days = ("sunday","monday","tuesday","wednesday","thursday","friday","daturday")
for i in days:
    print(i)

print(days[2])


# Create a tuple of your favorite colors and print it. Check if a certain color is present in the
# tuple and print the result.

colors = ("blue","black","pink","red")
color_to_check= input("enter the color you want to check:\n")


if color_to_check in colors :
    index = colors.index(color_to_check)
    print(f"{color_to_check} is found at index {index}")
    
else:
    print("not found")


# Create a dictionary representing the information of a book with keys "title", "author", and
# "year" and print it. Update the year of the book and print the updated dictionary.

book = {"title " : " God of thunder",
        "author" : "Beni Raj Karki",
        "year": 2005 }
print(type(book))

if "year" in book:
    print(f"initail year avalue {book['year']}")
    book["year"] = 1990
    print(f"updated year {book['year']}")

print(book.values())

# Create a dictionary containing the names of fruits as keys and their corresponding colors
# as values and print it. Add a new fruit-color pair to the dictionary and print the updated
# dictionary.

fruits = {
    "banana" :  "yellow",
    "orange" : "orange",
    "apple" : "red",
    "kiwi" : "green"
}
print(fruits.values())
fruits["grape"] = "purple"
print(fruits)


# Create a dictionary representing the population of different cities with keys as city names
# and values as population numbers and print it. Remove a city from the dictionary and print
# the modified dictionary.

population = {
    "kathmandu" : 198900,
    "birtamod" : 60000,
    "Gaighat" : 90000,
    "dhran" : 100000
}

print(population)
population.pop("kathmandu")
print(population)
