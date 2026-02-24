# songs = ["Iwo Loba", "Osuba", "Beautiful things", "Not like us", "Holy words"]
# print(songs[2])
# songs[3] = songs[3].upper()
# print(songs)
# print("Osuba" in songs)
# songs.append("Rainbow")
# print(songs)
# songs.insert(1, "Saved My Life")
# print(songs)
# songs.remove("Iwo Loba")
# print(songs)
# print(songs[:3])




# Monday assignment 1 - 32

# 1. Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
# fruits = ["apple", "banana", "orange"]
# print(fruits[0])

# 2. Create a list called colors with items "red", "green", "blue". Print the last item using negative
# indexing.
# colors = ["red", "green", "blue"]
# print(colors[-1])

# 3. Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7 (inclusive
# of index 3, exclusive of 8).
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[3:8])

# 4. Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3
# # to the end.
# alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# print(alphabets[-3:])

# 5. Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
# ages = [20, 30, 40]
# ages[1] = 35
# print(ages)

# 6. Create a list called grades with items "A", "B", "C", "D". Replace the items from index 1 (inclusive) 
# # to index 3 (exclusive) with "X".
# grades = ["A", "B", "C", "D"]
# grades[1:3] = ["X"]
# print(grades)

# 7. Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning 
# of the list.
# cities = ["New York", "London", "Paris"]
# cities.insert(0, "Tokyo")
# print(cities)

# 8. Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the
# list.
# fruits =  ["apple", "banana", "cherry"]
# print(len(fruits))

# 9. Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
# prices = [10.5, 20.0, 15.75]
# print(type(prices))

# # 10. Create a list called mixed with items 10, "apple", True. Print the list.
# mixed = [10, "apple", True]
# print(mixed)

# 11. Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
# tuple_data = "a", "b", "c"
# tuple_data = list(tuple_data)
# print(tuple_data)

# 12. Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
# books = ["Python", "Java"]
# books.append("JavaScript")
# print(books)

# 13. Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
# names = ["Alice", "Bob", "Eve"]
# names.insert(1, "Charlie")
# print(names)

# 14. Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 
# with list2.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# 15. Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") 
# to students.
# students = ["Alice", "Bob"]
# students.extend(("Charlie", "David"))
# print(students)

# 16. Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
# colors = ["red", "green", "blue"]
# colors.remove("green")
# print(colors)

# 17. Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item 
# at index 2.
# numbers = [10, 20, 30, 40]
# del numbers[2]
# print(numbers)

# 18.	Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
# fruits = ["apple", "banana", "cherry"]
# fruits.clear()
# print(fruits)

#  19.	Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
# names = ["Zoe", "Alice", "Bob"]
# names.sort()
# print(names)

#  20. 	Create a list called ages with items 25, 35, 20. Sort the list in descending order.
# ages = [25, 35, 20]
# ages.sort(reverse = True)
# print(ages)

#  21. 	Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
# words = ["Apple", "banana", "Orange"]
# words.sort(key = str.lower)
# print(words)

#  22. 	Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
# numbers = [1, 2, 3, 4]
# numbers.sort(reverse = True)
# print(numbers)

#  23.	Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
# 	slicing.
# letters = ["a", "b", "c", "d"]
# print(letters[::-1])

#  24.	Create a list called original with items "one", "two", "three". Create a copy of the list.
# original = ["one", "two", "three"]
# copied = original.copy()
# print(copied)

#  25.	Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
# 	list2 together.
# list1 = ["a", "b"]
# list2 = ["c", "d"]
# list1.extend(list2)
# print(list1)

#  26.	Access and print the second subject of the first person in the list.
# 	data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
# data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
# print(data[0][1])

#  27.	Access and print the first value in the list of numbers associated with "San Francisco".
# 	records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]
# records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]
# print(records[1][1][0])

# 28.	Get the first e in Ayo’s gender and Get Ben’s age.
#  	group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
# group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
# print(group[0][1][0])
# print(group[1][1][1])

#  29.	Get the l in Nina’s gender and Get Tobi’s age
# 	records = [
#     ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]
# records = [
#     ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]
# print(records[1][1][0][4])

#  30.	Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the 
# battery percentage of R2
# robot_grid = [
#     ["R2", ["battery", [98]]],
#     ["R5", ["status", "active"]],
#     ["X1", [["joint", "loose"], "error"]]
# ]
# robot_grid = [
#     ["R2", ["battery", [98]]],
#     ["R5", ["status", "active"]],
#     ["X1", [["joint", "loose"], "error"]]
# ]
# print(robot_grid[2][1][0][1][1:3])
# print(robot_grid[0][1][1][0])
#  31.	Get the Five in the Jazz song title and Get the duration of the Jazz song
# playlist = [
#     ["Jazz", ["Take Five", 5.24]],
#     ["Pop", ["Blinding Lights", 3.20]],
#     ["Rock", ["Bohemian Rhapsody", 5.55]]
# ]
# playlist = [
#     ["Jazz", ["Take Five", 5.24]],
#     ["Pop", ["Blinding Lights", 3.20]],
#     ["Rock", ["Bohemian Rhapsody", 5.55]]
# ]
# print(playlist[0][1][0])
# print(playlist[0][1][1])


#  32.	Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
# animals = [
#     ["Elephant", ["Herbivore"]],
#     ["Tiger", ["Carnivore"]],
#     ["Frog", ["Amphibian"]]
# ]
# animals = [
#     ["Elephant", ["Herbivore"]],
#     ["Tiger", ["Carnivore"]],
#     ["Frog", ["Amphibian"]]
# ]
# print(animals[1][1][0][-4])
# print(animals[2][1][0][0])



# TUPLES



# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, pos), (dept1, dept2) = record
# _, (age, _), (dept1, _) = record

# print(age)
# print(dept1)




# order = (
#     "ORD-2049",
#     {
#         "customer": ("Alice", 24),
#         "delivery": ("Lagos", ("Ikeja", 1000))
#     },
#     ["Laptop", "Mouse", "Keyboard"]
# )


# Using tuple unpacking and nested destructuring only, extract:
# The customer’s age
# The delivery city (e.g. "Ikeja")
# The first item in the order

# Ignore all other values.

# Expected Output:
# 24
# Ikeja
# Laptop


# record = (
#     "STD-8821",
#     ("John", (19, "Computer Science")),
#     [("Math", 78), ("Physics", 85), ("Chemistry", 69)]
# )

# _, (name, (_, _)), ((_, _,) (_, score), (_, _))  = record
# print(name)
# print(score)

# trip = (
#     "TRP-450",
#     ("Peace Bus", ("Abuja", "Kaduna")),
#     (
#         ("Driver", ("Samuel", 45)),
#         ("Conductor", ("Amina", 32))
#     ),
#     [12000, 13500, 15000]
# )
# _, (_, (_, destination)), ((_), (job2, (_))), [_, _, _] = trip
# print(destination)
# print(job2)



# Tuesday Assignment
# 1. Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.
# dimensions = (10, 20, 30)
# length, width, height = dimensions 
# print(length)
# print(width)
# print(height)

# 2. Given the tuple coordinates:
# Unpack the tuple into variables x, y, and z, and print the value of y.
# coordinates = (1.5, 2.5, 3.5)
# coordinates = (1.5, 2.5, 3.5)
# x, y, z = coordinates
# print(y)

# 3. Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into 
# variables name, age, and profession, and print the value of profession.
# person = ("John", 25, "Engineer")
# name, age, profession = person
# print(profession)

# 4. Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# (student1, student2), *_ = data
# print(student2)

# 5. Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two 
# values into variables color1 and color2, and print both variables.
# colors = ("red", "green", "blue", "yellow")
# color1, color2, *_ = colors
# print(color1)
# print(color2)

# 6. Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments.
# Print the extracted age and the first department.
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age_and_position), (departments) = record
# print(age_and_position[0])
# print(departments[0])

# 7. Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables 
# and print the value of the second variable.
# triplet = ("one", "two", "three")
# first, second, third = triplet
# print(second)

# 8. Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category 
# and the manufacture year.
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# product_id, (category, price), (manufacture_date) = info
# manufacture_day, manufacture_month, manufacture_year = manufacture_date
# print(category)
# print(manufacture_year)

# 9. Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack 
# the nested tuples into individual variables and print the second value of the third tuple.
# nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
# (first_nest), (second_nest), (third_nest) = nested_tuple
# print(third_nest[1])

# 10. Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
# inventory = (("apples", 50), ("banana", 100), ("cherries", 75))
# (fruit1, quantity1), (fruit2, quantity2), (fruit3, quantity3) = inventory
# print(quantity2)



# Wednesday class


# Dictionaries


# Class Exercise


# states_and_capitals = {"Ondo": "Akure", "Kwara": "Ilorin", "Imo": "Owerri", "Osun": "Osogbo", "Anambra": "Awka"}
# print(states_and_capitals) 

# states_and_capitals["Lagos"] = "Ikeja"
# print(states_and_capitals) 

# states_and_capitals["Osun"] = states_and_capitals["Osun"].upper()  
# print(states_and_capitals) 

# del states_and_capitals["Ondo"]
# print(states_and_capitals) 




# 1st ASSIGNMENT

# 1. Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".
# student = {"name": "John", "age": 20, "grade": "A"}
# print(student["name"])


# 2. Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
# product = {"name": "Laptop", "price": 999.99, "stock": 50}
# product["price"] = 899.99
# print(product)


# 3.Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
# employee = {"name": "Alice", "position": "Manager"}
# employee["salary"] = 50000
# print(employee)


# 4. Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
# inventory = {"apple": 10, "banana": 5, "orange": 8}
# del inventory["banana"]
# print(inventory)


# 5. Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
# person = {"name": "Bob", "age": 25, "city": "New York"}
# person_copy = person.copy()
# print(person)
# print(person_copy)


# 6. Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
# family = {"child1": {"name": "Vee", "age": 24} , "child2": {"name": "Von", "age": 18} , "child3": {"name": "Violet", "age": 14}}
# print(family["child2"]["age"])


# 7. Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
# car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
# print(car["model"])


# 8. Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
# settings = {"volume": 50, "brightness": 75, "language": "English"}
# settings["language"] = "Spanish"
# print(settings)


# 9. Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
# scores = {"math": 90, "science": 85, "english": 88}
# del scores["science"] 


# 10. Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
# menu = {"starter": "Soup", "main_course": "Steak", "dessert": "Ice Cream"}
# print("appetizer" in menu)


# # 11. Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
# config = {"theme": "dark", "language": "English", "timezone": "UTC"}
# config.clear()
# print(config)


# 12.	Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
# phone_book = {"Alice": "09098309099", "Bob": "07198089090", "Charlie": "08134545667"}
# print(len(phone_book))


# 13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
# grades = {"math": "A", "science": "B", "history": "C"}
# print(list(grades.keys()))

# 14. 	Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.
# employee = {"name": "David", "position": "Engineer", "salary": 70000}
# print(list(employee.values()))



# 15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
# game = {"title": "Minecraft", "genre": "Sandbox", "rating": 4.5}
# print(list(game.items()))



# 2nd ASSIGNMENT

# ===============================
# Nested Dictionary Modification Exercises
# ===============================

# # Q1. Given this dictionary, change the "math" score to 95.
# student = {
#     "name": "Alice",
#     "scores": {"math": 80, "english": 85}
# }
# Expected Output:
# {'name': 'Alice', 'scores': {'math': 95, 'english': 85}}
# student["scores"]["math"] = 95
# print(student)

# Q2. Add a new subject "science" with score 90 inside "scores".
# student = {
#     "name": "Alice",
#     "scores": {"math": 80, "english": 85}
# }
# Expected Output:
# {'name': 'Alice', 'scores': {'math': 80, 'english': 85, 'science': 90}}
# student["scores"]["science"] = 90
# print(student)


# Q3. Change the author's name of "Python 101" to "Mike".
# library = {
#     "Python 101": {"author": "Tom", "year": 2020},
#     "Data Science": {"author": "Jane", "year": 2021}
# }
# Expected Output:
# {'Python 101': {'author': 'Mike', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021}}
# library["Python 101"]["author"] = "Mike"
# print(library)


# Q4. Add a new key "publisher" = "O'Reilly" to "Data Science".
# library = {
#     "Python 101": {"author": "Tom", "year": 2020},
#     "Data Science": {"author": "Jane", "year": 2021}
# }
# Expected Output:
# {'Python 101': {'author': 'Tom', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021, 'publisher': "O'Reilly"}}
# library["Data Science"]["publisher"] = "O'Reilly"
# print(library)


# Q5. In this dictionary, add a new phone number "work": "555-999" for Alice.
# contacts = {
#     "Alice": {"home": "555-123", "mobile": "555-456"},
#     "Bob": {"home": "555-789"}
# }
# Expected Output:
# {'Alice': {'home': '555-123', 'mobile': '555-456', 'work': '555-999'}, 'Bob': {'home': '555-789'}}
# contacts["Alice"]["work"] = "555-999"
# print(contacts)

# Q6. Change Bob’s "home" number to "555-000".
# contacts = {
#     "Alice": {"home": "555-123", "mobile": "555-456"},
#     "Bob": {"home": "555-789"}
# }
# Expected Output:
# {'Alice': {'home': '555-123', 'mobile': '555-456'}, 'Bob': {'home': '555-000'}}

# contacts["Bob"]["home"] = "555-000"
# print(contacts)


# Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
# into the list of students.
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 70}},
#  {'name': 'Eve', 'scores': {'math': 88, 'english': 92}}]
# students.extend([{"name": "Eve", "scores": {"math": 88, "english": 92}}])
# print(students)


# Q8. Change Bob's english score from 70 to 78.
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]
# students[1]["scores"]["english"] = 78
# print(students)

# Q9. Add a new dictionary  
# inside Alice’s record under a new key "enrollment".
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 78}}
# ]
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}, 'enrollment': {'year': 2022, 'semester': 'Spring'}}, {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]
# students.extend(["enrollment"]{"year": 2022, "semester": "Spring"})
# students[0].update({'enrollment': {'year': 2022, 'semester': 'Spring'}})
# print(students)

# Q10. In this shop cart, add a new product "Notebook" with price 200.
# cart = {
#     "items": [
#         {"name": "Pen", "price": 10},
#         {"name": "Book", "price": 50}
#     ],
#     "owner": "Alice"
# }
# Expected Output:
# {'items': [{'name': 'Pen', 'price': 10}, {'name': 'Book', 'price': 50}, {'name': 'Notebook', 'price': 200}],
#  'owner': 'Alice'}
# cart["items"].append({"name": "Notebook", "price": 200})
# print(cart)



# WEEKEND ASSIGNMENT


# 1. Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in 
# the set and print the result.
fruits = {"air", "water"}
print("food" in fruits)


# 2. Create a set called colors with values {"red", "green", "blue"}. Add the color "yellow" 
# to the set and print the updated set.
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)


# 3. Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to 
# the set and print the updated set.
animals = {"cat", "dog", "rabbit"}
animals.update(["horse", "sheep"])
print(animals)


# 4. Create a set called countries with values {"USA", "Canada", "Mexico"}. Remove "Canada" from the 
# set and print the updated set.
countries = {"USA", "Canada", "Mexico"}
countries.remove("Mexico")
print(countries)


# 5. Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in
# the set without raising an error.
cities = {"New York", "Los Angeles", "Chicago"}
cities.discard("Houston")
print(cities)


# 6. Given the list seasons = ["Spring", "Summer", "Fall", "Winter", “Spring”], convert the list to 
# a set to get rid of the duplicate `Spring`.
seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
seasons = set(seasons)
print(seasons)


# 7. Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets 
# and print the result.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)


# 8. Given two sets, setA = {"a", "b", "c"} and setB = {"c", "d", "e"}, find the intersection of the 
# sets and print the result.
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
setC = setA.intersection(setB)
print(setC)


# 9. Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print 
# the updated set.
prime_numbers = {2, 3, 5, 7}
prime_numbers.add(11)
print(prime_numbers)


# 10. Given the set odd_numbers = {1, 3, 5, 7, 9}, remove a random item from the set and print the 
# updated set.
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers.pop()
print(odd_numbers)


# 11. Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result.
vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)


# 12. Given the set letters = {"a", "b", "c"}, find the difference between `letters` and 
# another set {"b", "c", "d"}. Print the result. Afterwards, find the symmetric difference and print the result.
letters = {"a", "b", "c"}
letters2 = {"b", "c", "d"}
difference = letters - letters2
print(difference)
symmetric_diff = letters ^ letters2
print(symmetric_diff)


# 13.	Create a set called tech_brands with values {"Apple", "Google", "Microsoft"}. 
# 	Add the items from another set {"Amazon", "Facebook"} and print the updated set 
# 	tech_brands without creating a new set.
tech_brands = {"Apple", "Google", "Microsoft"}
other_brands = {"Amazon", "Facebook"}
tech_brands.update(other_brands)
print(tech_brands)


#  14. 	Create a set called students with values {"Alice", "Bob", "Charlie", "David"}. Use the 
# 	remove method to remove "Charlie" from the set and print the updated set. Then try to 
# 	remove "Eve" from the set and observe the behavior.
# students = {"Alice", "Bob", "Charlie", "David"}
# students.remove("Charlie")
# print(students)
# students.remove("Eve")
# print(students)
# KeyError: 'Eve'



#  15. 	Given a list numbers_list = [1, 2, 3, 4, 4, 5, 5], convert this list to a set to remove 
# 	duplicates and print the resulting set.
numbers_list = [1, 2, 3, 4, 4, 5, 5]
numbers_list = set(numbers_list)
print(numbers_list)


#  16. 	Given a string text = "hello", convert this string to a set to find the unique 
# 	characters and print the resulting set.
text = "hello"
text = set(text)
print(text)


#  17. 	Create a set called vehicles with values {"car", "bike", "bus", "train"}. Find out how 
# 	many items are in the set and print the result.
vehicles = {"car", "bike", "bus", "train"}
print(len(vehicles))


#  18. 	Given the set gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}, print the 
# 	number of items in the set.
gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}
print(len(gadgets))

