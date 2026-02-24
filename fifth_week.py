# ----------------------------------------------------------ASSIGNMENT ----------------------------------------------------


# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.

# from random import randint

# secret_number = randint(1, 100)

# attempts = 5

# while attempts >= 1:
#     guess = int(input("Guess the secret number between 1 and 100: "))

#     if not(1 <= guess <= 100):
#         print("Invalid guess. It must be between 1 and 100")
#         continue

#     if guess == secret_number:
#         print("Congratulations!!! 🎉🥳. You guessed the secret number correctly")
#         break

#     if guess < secret_number:
#         print("You guessed too low.")
#     else:
#         print("You guessed too high.")

#     attempts -= 1
#     print(f'You have {attempts} attempts left')
# else:
#     print(f"You used up all your attempts. The secret number is {secret_number}. Better luck next time 😭")


# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# SECRET_PASSWORD = "secret"

# while True:
#     password = input("Enter the secret password: ").strip()

#     if password == SECRET_PASSWORD:
#         print("Correct password.")
#         break

#     print("Invalid password")


# SECRET_PASSWORD = "secret"

# password = ''

# while password != SECRET_PASSWORD:
#     password = input("Enter the secret password: ").strip()

#     if password == SECRET_PASSWORD:
#         print("Correct password.")
#         break

#     print("Invalid password")



# 8. Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.

# hello my name is Winnie

# (8)
# text = input("Enter some text: ").strip()

# i = 0

# # vowels = "aeiouAEIOU"
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# no_of_vowels = 0

# while i < len(text):
#     char = text[i]

#     if char in vowels:
#         no_of_vowels += 1

#     i += 1

# print(f"No of vowels: {no_of_vowels}")




# 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().

# text = input("Enter some text: ").strip()

# reversed_text = []

# # python -> nohtyp

# i = len(text) - 1

# while i >= 0:
#     char = text[i]
#     reversed_text.append(char)
#     i -= 1

# print("".join(reversed_text))


# text = input("Enter some text: ").strip()

# # python

# i = 0

# reversed_text = []

# while i < len(text):
#     char = text[i]
#     reversed_text.insert(0, char)
#     i += 1

# print("".join(reversed_text))


# text = input("Enter some text: ").strip()

# # python

# i = 0

# reversed_text = ""

# while i < len(text):
#     char = text[i]
#     reversed_text = char + reversed_text
#     i += 1

# print(reversed_text)

# 10. Write a program that takes comma-separated integers from the user, converts that
# to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
# Use the min() function.

# numbers = tuple(input("Enter comma-separated numbers: ").split(","))

# smallest = int(numbers[0])

# i = 1

# while i < len(numbers):
#     current_num = int(numbers[i])

#     if current_num < smallest:
#         smallest = current_num
    
#     i += 1

# print(f"{smallest} is the minimum")


# 11. Write a program that takes a string input from the user and uses a while loop to count
# the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}





# -------------------------------------------FOR LOOPS----------------------------------------------------------


# colors = ("red", "blue", "green", "yellow")

# for color in colors:
#     print(color.capitalize())

# import string
# # print(string.ascii_lowercase_cons)
# name = "Adil".lower()
# for letter in name :
#     if letter in string.ascii_lowercase and letter not in ["a", "e", "i", "o", "u"]:
#         print(letter)


# actions = ["wake up", "walk", "skip", "run", "talk", "stop", "land"]
# for action in actions:
#     if action != "skip":
#         print(action)
#     else:
#         continue

# for action in actions:
#     if action != "stop":
#         print(action)
#     else:
#         break



# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# for i in range(len(means_of_transportation)):
#     means_of_transport = means_of_transportation[i]
#     print(f"{i + 1}. {means_of_transport}")



# number = int(input("Enter a number for the multiplication table: "))
# for i in range(1, 13):
#     result = number * i
#     print(f"{number} x {i} = {result}")



# phrase = input("Enter a phrase: ").strip().split()
# acronym = []
# for word in phrase:
#     acronym.append(word[0].capitalize())
# print("".join(acronym))











# ----------------------------------------------------ASSIGNMENT-----------------------------------------------------




# 1. Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)

# num = (input("Enter a number: "))
# sum_of_nums = 0
# # for i in range(num + 1):
# #     sum_of_nums += i

# # print(sum_of_nums)
# for i in range(len(num)):
#     add = num[i]
#     sum_of_nums += int(add)

# print(sum_of_nums)


# 2. Collect a string from the user and use loops to count the number of vowels and consonants in the string. 
# Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# import string
# sentence = input("Enter a string: ")
# letters = string.ascii_letters
# vowels = "aeiouAEIOU"
# vowel = 0
# cons = 0
# for char in sentence:
#     if char in letters and char not in vowels:
#         cons += 1
#     elif char in letters and char in vowels:
#         vowel += 1

# print(f"Vowels: {vowel}, Consonant: {cons}")  



# 3. Write a program that takes an integer input from the user and prints the multiplication table for that 
# number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60


# number = int(input("Enter a number for the multiplication table: "))
# for i in range(1, 13):
#     result = number * i
#     print(f"{number} x {i} = {result}")



# 4. Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not 
# reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"


# string = input("Enter a string to reverse: ").strip()
# arrange = []
# for i in range(1, len(string) + 1):
#     char = arrange.append(string[-i])
# print("".join(arrange))



# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and 
# removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# nums = input("Enter a list of numbers seperated by commas: ").strip().split(",")
# unique = []
# for num in nums:
#     if num not in unique:
#         unique.append(num)

# print(unique)


# 6.	Write a program that takes an integer input n from the user and prints the first 
# 	n numbers in the Fibonacci sequence. Example:
# 	Input: 10
# 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# n = int(input("Enter a number: "))
# fib_list = []

# fibonacci = 0
# for i, j in range(n):
#     fibonacci = fibonacci + i + j
#     print(fibonacci)




#  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20

# nums = int(input("Enter a list of numbers seperated by a comma: ")).strip().split(",")
# greatest = 0
# i = 0
# for i in range(len(nums)):
#     num = nums[i]
#     greatest = num > greatest

# print(greatest)




#  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

# n = int(input("Enter a number: "))
# sum_of_n = 0
# # print(list(range(0, n + 2, 2)))
# for i in range(0, n + 2, 2):
#     sum_of_n += i
# print(sum_of_n)



#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1

# text = input("Enter a sting: ")




# 10.	Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)

# n = int(input("Enter a number: "))
# sum_of_squares = 0
# # print(list(range(n)))
# for i in range(n + 1):
#     sum_of_squares += (i ** 2)
# print(sum_of_squares)



#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"

# phrase = input("Enter a phrase: ").strip().split()
# acronym = []
# for word in phrase:
#     acronym.append(word[0].capitalize())
# print("".join(acronym))


#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4

# string = input("Enter a string: ").strip().split()
# num_of_words = 0
# for word in string:
#     num_of_words += 1
# print(num_of_words)



#  13. 	Collect a string from the user and only print out the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this Sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence

# string = input("Enter a sentence: ").lower().strip().split()
# for word in string:
#     if word.startswith("s"):
#         print(word)


#  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.

# for i in range(2, 21, 2):
#     print(i)


#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.

# num1_to_50 = list(range(1, 50))
# divisible_by_3 = [num for num in num1_to_50 if num % 3 == 0]
# print(divisible_by_3)



# divisible = []
# for i in range(1, 51):
#     if i % 3 == 0:
#         divisible.append(i)
# print(divisible)


# 16.	Go through the string below and if the length of a word is even, print that word.
# 	st = ‘Print every word in this sentence that has an even number of letters’
# 	Output: 
# 	word
# 	in
# 	this
# 	sentence
# 	that
# 	an
# 	even
# 	number
# 	of

# st = "Print every word in this sentence that has an even number of letters".split()
# for word in st:
#     if len(word) % 2 == 0:
#         print(word)



#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


#  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# for name, grade in zip(names, grades):
#     print(f"{name} got grade {grade}")



# 19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

# for i in range(0, len(items), 2):
#     print(f"{i}: {items[i]}")


#  20.	Given two lists of numbers of the same length, print the indices and values
#  	of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]

# empty = []
# for i in range(len(list1)):
#     if list1[i] != list2[i]:
#         empty.append(f"Index {i}: {list1[i]} != {list2[i]}")

# print(empty)




# ------------------------------------LIST COMPREHENSION---------------------------------------------------



# colors = ["red", "green", "purple", "brown", "silver"]
# colors_len = [len(color) for color in colors]
# print(colors_len)


# brands = ["Gucci", "Aquafina", "Samsung", "Apple", "D & G", "Nike", "New Balance", "Adidas"]
# starts_with_vowel = [brand.lower().startswith(("a", "e", "i", "u", "o")) for brand in brands]
# print(starts_with_vowel) 


# numbers = [9, 2, 9, 7, 1, 3]
# squares = [number ** 2 for number in numbers]
# print(squares)



# numbers = [9, 3, 8, 10, 25, 7, 53]
# odd_nums = [number for number in numbers if number % 2 != 0]
# print(odd_nums)




# brands = ["Gucci", "Aquafina", "Samsung", "Apple", "D & G", "Nike", "New Balance", "Adidas"]
# at_least_5 = [brand for brand in brands if len(brand) <= 5]
# print(at_least_5)



# countries = ["Nigeria", "USA", "Ghana", "Russia", "Singapore", "Kenya", "Brazil", "Togo"]
# developing_countries = ["Nigeria", "Ghana", "Kenya", "Togo"]
# developed_countries = [country for country in countries if country not in developing_countries]
# print(developed_countries)








# WEDNESDAY ASSIGNMENT



# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
# digits = [1, 2, 3, 4, 5]
# squares = [num ** 2 for num in digits]
# print(squares)


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
# names = ["John", "Sara", "Mike", "Amanda"]
# start_with_a = [name for name in names if "a" in name.lower()]
# print(start_with_a)


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
# values = [5, 12, 3, 18, 7]
# greater_than_10 = [value > 10 for value in values]
# print(greater_than_10)


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
# animals = ["dog", "cat", "lion", "tiger"]
# last_char = [animal[-1] for animal in animals]
# print(last_char)


# 12. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
# nums = [2, 4, 6, 8]
# triple_num = [num * 3 for num in nums]
# print(triple_num)



# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
# greetings = ["HELLO", "WORLD", "PYTHON"]
# lowercase = [greeting.lower() for greeting in greetings]
# print(lowercase)



# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
# items = ["sky", "tree", "rock", "stone"]
# contains_e = [item for item in items if "e" in item.lower()]
# print(contains_e)





# ------------------------------------LIST COMPREHENSION---------------------------------------------------


# -------------------------------------DICTIONARY COMPREHENSION-----------------------------------------------


# foods = ["Yam", "Egg", "Afaang", "amala", "Abula", "avocado", "Almond"]

# starts_with_a = {food: food.lower().startswith("a") for food in foods}
# print(starts_with_a)




# 5, 6, 7, 13



# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
# values = [5, 12, 3, 18, 7]
# greater_than_10 = all(value > 10 for value in values)
# print(greater_than_10)


# # 6. Is there any name that contains the letter 'a'?
# # Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: True
# names = ["John", "Sara", "Mike", "Amanda"]
# contains_a = any("a" in name.lower() for name in names)
# print(contains_a)

# # 7. Are all the words made up of only uppercase letters?
# # Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# # Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
# all_uppercase = all(greeting.isupper() for greeting in greetings) 
# print(all_uppercase)

# # 13. Are all temperatures above 0°C?
# # Input: [12, 7, 3, -1, 5]
# # Expected Output: False
# temperatures = [12, 7, 3, -1, 5]
# greater_than_0 = all(temperature > 0 for temperature in temperatures)
# print(greater_than_0)




# def talk():
#     print("I am talking")

# talk()

# def to_upper(name):
#     print(name.upper())

# to_upper("adil")



# def raise_to_power(base, exponent):
#     print(base ** exponent)

# raise_to_power(2, 3)









# ------------------------------------------------WEEKEND ASSIGNMENT----------------------------------------------


# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]
any_starts_with_z = any(word.lower().startswith("z") for word in words)
print(any_starts_with_z)


# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
any_contains_org = any(".org" in email for email in emails)
print(any_contains_org)


# 10. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
values = [1, 3, 5, 7, 9]
all_odd = all(value % 2 != 0 for value in values)
print(all_odd)


# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
words = ["hi", "dog", "go", "sun"]
all_longer_than_2 = all(len(word) > 2 for word in words)
print(all_longer_than_2)


# 14. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
fruits = ["banana", "mango", "kiwi", "grape"]
vowels = "aeiou"
all_ends_with_vowel = all(fruit[-1] in vowels for fruit in fruits)
print(all_ends_with_vowel)



# 16. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
numbers = [5, -2, 3, 0, 8]
any_num_less_than_0 = any(num < 0 for num in numbers)
print(any_num_less_than_0)



# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
names = ["Alice", "Bob", "charlie", "David"]
all_starts_with_upper = all(name[0].isupper() for name in names)
print(all_starts_with_upper)



# 19. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
sentences = ["Short one", "This is a much longer sentence", "Okay"]
any_longer_than_20 = any(len(sentence) > 20 for sentence in sentences)
print(any_longer_than_20)