# my_list = ["James", "Janet", "Jack", "Jill"]

# for name in my_list:
#     print(name)


# wild_animals = ["snake", "lion", "dog", "goat", "hen"]

# for animal in wild_animals:
#     print(animal)

# wild_animals = ["snake", "lion", "dog", "goat", "hen"]

# for wild_animal in wild_animals:
#     print(wild_animals)

# ['snake', 'lion', 'dog', 'goat', 'hen']
# ['snake', 'lion', 'dog', 'goat', 'hen']
# ['snake', 'lion', 'dog', 'goat', 'hen']
# ['snake', 'lion', 'dog', 'goat', 'hen']
# ['snake', 'lion', 'dog', 'goat', 'hen']


# wild_animals = ["snake", "lion", "dog", "goat", "hen"]

# for evydnjefnnf in wild_animals:
#     print(evydnjefnnf)

# import string

# name = "Winnie!"

# vowels = "AEIOUaeiou"

# alphabets = string.ascii_letters

# for char in name:
#     if char not in vowels and char in alphabets:
#         print(char)


# print(list(range(2, 9)))


# for number in range(2, 9):
#     print(number)


# for wild_animal in ["snake", "lion", "dog", "goat", "hen"]:
#     print(wild_animal)


# for num in [1, 2, 3]:
#     print(num)

# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}

# capitals = list(capitals.items())

# print(capitals)

# i = 0

# while i < len(capitals):
#     country, capital = capitals[i]
#     print(f"The capital of {country} is {capital}")
#     i += 1


# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}


# for country, capital in capitals.items():
#     print(f"The capital of {country} is {capital}")


# for animal in {'snake', 'lion', 'dog', 'goat', 'hen'}:
#     print(animal)

actions = ["wake up", "walk", "skip", "run", "talk", "stop", "land"]

# 1. Loop through the actions, but skip "skip"

# Output:

# "wake up"
# "walk"
# "run"
# "talk"
# "stop"
# "land"


# for action in actions:
#     if action == "skip":
#         continue
#     print(action)

# 2. Stop right before stop

# Output:

# "wake up"
# "walk"
# "skip"
# "run"
# "talk"

# for action in actions:
#     if action == "stop":
#         break
#     print(action)



# print(list(range(3, 100, 5)))

# print(list(range(10, -1, -1)))
# for i in range(10, -1, -2):
#     print(i)


# print(list(range(8)))

# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# for i in range(len(means_of_transportation)):
#     means_of_transport = means_of_transportation[i]
#     print(f"The element at index {i} is {means_of_transport}")

# The element at index 0 is airplane
# The element at index 1 is jet
# The element at index 2 is train


# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# for i in range(len(means_of_transportation)):
#     means_of_transport = means_of_transportation[i]
#     print(f"{i+1}. {means_of_transport}")


# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# print(list(enumerate(means_of_transportation)))


# for (index, means_of_transport )in enumerate(means_of_transportation, start=1):
#     print(index)
#     print(means_of_transport)


# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# for i in range(len(means_of_transportation)):
#     means_of_transport = means_of_transportation[i]
#     print(f"{i+1}. {means_of_transport}")


# 1. airplane
# 2. jet
# 3. train
# 4. car
# 5. camel
# 6. broom


# ingredients = {"maggi", "pepper", "ginger", "salt", "tumeric", "curry", "cinnamon"}
# ingredients = {}

# for ingredient in ingredients:
#     print(ingredient)
# else:
#     print("Loop has ended")



# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adj in adjectives:
#     for animal in animals:
#         print(adj, animal)


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]


# print(list(zip(adjectives, animals)))
# for adj, animal in zip(adjectives, animals):
#     print(f"{adj} {animal}")

# adjectives = ["fierce", "majestic", "playful", "happy", "sad"]
# animals = ["lion", "eagle", "dolphin"]

# for adj, animal in zip(adjectives, animals):
#     print(f"{adj} {animal}")


# adjectives = ["fierce", "majestic", "playful", "happy", "sad"]
# animals = ["lion", "eagle", "dolphin"]


# shortest = min(adjectives, animals, key=len)

# for i in range(len(shortest)):
#     adj = adjectives[i]
#     animal = animals[i]
#     print(f"{adj} {animal}")



# name = "Felix"

# if name == "James":
#     pass


# print("End of file")



# name = "Felix"

# for char in name:
#     pass



# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60


# 11. Collect a phrase from the user and use a loop to generate an acronym by taking the first
# letter of each word. Print the acronym. Example:
# Input: "Portable Network Graphics"
# Output: "PNG"



# ---------------------------------------------ASSIGNMENT CORRECTION------------------------------------------------------


# 4. Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"


# my_list = ["bag", "onions", "pen", "shoes"]

# print(list(reversed(my_list)))

# name = "Kenneth"

# print("".join(reversed(name)))

# text = input("Enter some text: ").strip()

# reversed_text = []

# for char in text:
#     reversed_text.insert(0, char)

# print("".join(reversed_text))

# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]


# numbers = input("Enter comma-separated numbers: ").split(",")

# print(numbers)

# unique_numbers = []

# for number in numbers:
#     if int(number) not in unique_numbers:
#         unique_numbers.append(int(number))
    
# print(unique_numbers)


# 6. Write a program that takes an integer input n from the user and prints the first 
# n numbers in the Fibonacci sequence. Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# fibonacci = [0, 1]

# n = int(input("Enter the fibonacci limit: "))

# for i in range(1, n-1):
#     second_number = fibonacci[i]
#     first_number = fibonacci[i-1]
#     third_number = first_number + second_number
#     fibonacci.append(third_number)

# print(fibonacci)



# 7. Collect a list of numbers from the user (entered as comma-separated values) and use a 
# loop to find and print the largest number in the list. Don’t use the built-in max 
# function or anything similar.
# Input: "10, 20, 5, 15"
# Output: 20


# 8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# even numbers from 1 to n. Print the sum.
# Input: 10
# Output: 30 (2 + 4 + 6 + 8 + 10)


# 9. Collect a string from the user and use a loop to count the frequency of each character 
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# Winnie


# inventory = {"yam": 5, "bread": 4, "chicken": 2}


# inventory["yam"] += 3

# inventory["onions"] = 10


# text = input("Enter some text: ").strip().lower()

# occurences = {}

# for i in range(len(text)):
#     char = text[i]
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1


# for char, occurence in occurences.items():
#     print(f"{char}: {occurence}")


# 10. Write a program that takes an integer n from the user and calculates the sum of 
# squares of all numbers from 1 to n. Print the sum. Example:
# Input: 3
# Output: 14 (1^2 + 2^2 + 3^2)
# Input: 5
# Output: 55 (1^2 + 2^2 + 3^2 + 4^2 + 5^2)


# n = int(input("Enter the value of n: "))

# result = 0

# workings = []

# for i in range(1, n+1):
#     square = i ** 2
#     result += square
#     workings.append(f"{i}^2")

# final_result = " + ".join(workings) + " = " + str(result)
# print(final_result)


# 11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# letter of each word. Print the acronym. Example:
# Input: "Portable Network Graphics"
# Output: "PNG"


# 12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# Print the count. Example:
# Input: "Hello world from Python"
# Output: 4

# words = input("Enter a phrase: ").split()
# print(words)

# no_of_words = 0

# for word in words:
#     no_of_words += 1

# print(no_of_words)


# 13. Collect a string from the user and only print out the words that start with the letter 
# ‘S’. Example:
# Input: “Print only the words that start with s in this Sentence”
# Output: 
# start
# s
# Sentence

# words = input("Enter some text: ").split()

# for word in words:
#     if word.upper().startswith("S"):
#         print(word)



# 14. 	Print all the even numbers from 1 to 20 using the range function and a loop.

# 15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# by 3.


# 16.	Go through the string below and if the length of a word is even, print that word.
# st = ‘Print every word in this sentence that has an even number of letters’
# Output: 
# word
# in
# this
# sentence
# that
# an
# even
# number
# of

# st = "Print every word in this sentence that has an even number of letters"

# words = st.split()

# for word in words:
#     if len(word) % 2 == 0:
#         print(word)




# 17. Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# “Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# are multiples of both three and five, print “FizzBuzz”.


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
    



# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

# 18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']


# print(list(zip(names, grades)))

# for name, grade in zip(names, grades):
#     print(f"{name} got grade {grade}")


# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B


# 19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

# items = ['shoe', 'stick', 'toy', 'fruit']

# print(list(enumerate(items)))

# for i, item in enumerate(items):
#     if i % 2 == 0:
#         print(f"{i}: {item}")



# 20. Given two lists of numbers of the same length, print the indices and values
# of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
# 'Index 1: 8 != 3',
# 'Index 3: 7 != 9',
# 'Index 5: 4 != 0',
# ]

# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# result = []

# for index, (first_num, second_num) in enumerate(zip(list1, list2)):
#     print(f"index: {index}")
#     print(f"first_num: {first_num}")
#     print(f"second_num: {second_num}")

#     if first_num != second_num:
#         result.append(f"Index {index}: {first_num} != {second_num}")

# print(result)

# ---------------------------------------------ASSIGNMENT CORRECTION------------------------------------------------------



# -----------------------------------LIST COMPREHENSIONS----------------------------------------

# my_list = ["James", "Janet", "Jack", "Jill"]

# my_list_upper = []

# for name in my_list:
#     my_list_upper.append(name.upper())

# print(my_list)
# print(my_list_upper)



# my_list = ["James", "Janet", "Jack", "Jill"]

# my_list_upper = [name.upper() for name in my_list]

# print(my_list)
# print(my_list_upper)



# colors = ["red", "green", "purple", "brown", "silver"]

# # [3, 5, 6, 5, 6]

# len_colors = [len(color) for color in colors]

# print(len_colors)



# brands = ["Gucci", "Aquafina", "Samsung", "Apple", "Dolce & Gabana", "Nike", "New Balance", "Adidas"]

# # [False, True, False, True, False, False, False, True]
# vowels = ("a", "e", "i", "o", "u")

# # starts_with_vowel = [brand.lower().startswith(vowels) for brand in brands]
# # print(starts_with_vowel)

# starts_with_vowel = [brand[0].lower() in vowels for brand in brands]
# print(starts_with_vowel)


# numbers = [9, 2, 9, 7, 1, 3]

# [81, 4, 81, 49, 1, 9]

# brands = ["Gucci", "Aquafina", "Samsung", "Apple", "Dolce & Gabana", "Nike", "New Balance", "Adidas"]
# vowels = ("a", "e", "i", "o", "u")
# consonant_brands = [brand for brand in brands if brand[0].lower() not in vowels]
# print(consonant_brands)
# consonant_brands = [brand.upper() for brand in brands if not brand.lower().startswith(vowels)]
# print(consonant_brands)



# numbers = [9, 3, 8, 10, 25, 7, 53]

# Get only the odd numbers


# brands = ["Gucci", "Aquafina", "Samsung", "Apple", "Dolce & Gabana", "Nike", "New Balance", "Adidas"]

# ["Gucci", "Apple", "Nike"]

# countries = ["Nigeria", "USA", "Ghana", "Russia", "Singapore", "Kenya", "Brazil", 'Togo']

# developing_countries = ["Nigeria", "Ghana", "Kenya", "Togo"]

# developed_countries




# -----------------------------------LIST COMPREHENSIONS----------------------------------------


# -----------------------------------ASSIGNMENT CORRECTION----------------------------------------

# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]

# names = ["John", "Sara", "Mike", "Amanda"]

# names_with_a = [name for name in names if "a" in name.lower()]

# print(names_with_a)


# -----------------------------------ASSIGNMENT CORRECTION----------------------------------------




# -----------------------------------SET COMPREHENSION----------------------------------------

# names = ["John", "Sara", "Amanda", "Mike", "Amanda"]

# names_with_a = {name for name in names if "a" in name.lower()}

# print(names_with_a)

# -----------------------------------SET COMPREHENSION----------------------------------------

# -----------------------------------DICTIONARY COMPREHENSION----------------------------------------

# names = ["John", "Sara", "Amanda", "Mike", "Amanda"]
# # [1, 2, 3, 2, 3]


# names = ["John", "Sara", "Amanda", "Mike", "Amanda"]
# {"John": 4, "Sara": 4, "Amanda": 6, "Mike": 4, "Amanda": 6}

# len_names = {name: len(name) for name in names}

# print(len_names)

# [1, 2, 3, 2, 3]

# vowels = "aeiouAEIOU"



# no_of_vowels = [sum([char in vowels for char in name]) for name in names]
# no_of_vowels = [[char in vowels for char in name] for name in names]

# print(no_of_vowels)


# foods = ["Yam", "Egg", "Afaang", "amala", "Abula", "Rice", "avocado", "Almond"]
# starts_with_a

# {"Yam": False. "Egg": False, "Afaang": True, "amala": True, "Abula": True, "Rice": False. "avocado": True, "Almond": True}


# food_starts_with_a = {food: food.lower().startswith("a") for food in foods}

# print(food_starts_with_a)


# print(all([False, True, False, True, True, False, True, False]))
# print(any([False, True, False, True, True, False, True, False]))
# print(any([False, False, False, False, False, False, False, False]))
# print(all([False, False, False, False, False, False, False, False]))
# print(all([True, True, True, True, True, True, True, True]))
# print(any([True, True, True, True, True, True, True, True]))


# -----------------------------------DICTIONARY COMPREHENSION----------------------------------------


# -----------------------------------GENERATORS----------------------------------------

# countries = ["Nigeria", "USA", "Ghana", "Russia", "Singapore", "Kenya", "Brazil", 'Togo']

# developing_countries = ["Nigeria", "Ghana", "Kenya", "Togo"]


# is_developed = [country not in developing_countries for country in countries]

# print(is_developed)

# Are they all developed?
# Is there any developing?

# are_all_developed = all([country not in developing_countries for country in countries])

# is_any_developing = any([country in developing_countries for country in countries])
# print(are_all_developed)
# print(is_any_developing)


# are_all_developed = all(country not in developing_countries for country in countries)
# is_any_developing = any(country in developing_countries for country in countries)
# print(are_all_developed)
# print(is_any_developing)

# 5, 6, 7, 13

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
# values = [5, 12, 3, 18, 7]
# values = [5, 2, 3, 8, 7]

# all_greater_than_10 = all(val > 10 for val in values)
# # all_greater_than_10 = all(val for val in values if val > 10)  # wrong

# print(all_greater_than_10)


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
# names = ["John", "Sara", "Mike", "Amanda"]

# contains_a = ("a" in name.lower() for name in names)

# print(any(contains_a))
# print(all(contains_a))



# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

# has_only_uppercase = all(greeting.isupper() for greeting in greetings)

# print(has_only_uppercase)

# months = ["JuLy", "October", "MaRch", "april", "AUGUST", "september"]

# at_least_1_has_at_least_1_upper = any(any(char.isupper() for char in month) for month in months)
# all_have_at_least_1_upper = all(any(char.isupper() for char in month) for month in months)

# print(at_least_1_has_at_least_1_upper)
# print(all_have_at_least_1_upper)

# 13. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False
# temperatures = [12, 7, 3, -1, 5]

# all_above_0 = all(temp > 0 for temp in temperatures)

# print(all_above_0)


# -----------------------------------GENERATORS----------------------------------------






