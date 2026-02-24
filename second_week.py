# # # # 1st assignment 10-16

# # # # 10.   Attempt to modify the character at index 2 in the string "Python" from question 9. Print the resulting error message.
# # # # word = "Python"
# # # # word[2] = "p"
# # # # TypeError: 'str' object does not support item assignment

# # # # 11.   Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.
# # x, y, z = "Orange", "Banana", "Cherry"
# # print(x)
# # print(y)
# # print(z)

# # # # 12.	Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# # # # single line.
# # age, name, is_student = 10, "John", True
# # print(age)
# # print(name)
# # print(is_student)
# # # #  13. 	Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.
# # x, y = 5, 10
# # y, x = x, y
# # print(y)
# # print(x)

# # # # # # 14. 	Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# # # # # # variables a, b, and c.
# # numbers = [1, 2, 3]
# # a, b, c = numbers
# # print(a)
# # print(b)
# # print(c)

# # # # # #  15. 	Convert a string variable called height from “1.35” to a float.
# # height = float("1.35")
# # print(type(height))

# # # # # #  16.	Predict the output of the following statements: 
# # # bool("")           #  False
# # # bool(123)          #  True
# # # bool(["apple", "cherry", "banana"])        #  True
# # # bool(False)        #  False
# # # bool(None)         #  False
# # # bool(0)            #  False
# # # bool("abc")        #  True
# # # bool(())           #  False
# # # bool([])           #  False
# # # bool({})           #  False    
# # # # 1st assignment 17 - 34
# # # # # # 17.	Convert a string “James John Kennedy” called “names” to a list using the string 
# # # # # # .split() method. Store the result in a list called “names_list”
# # names = "James John Kennedy"
# # result = (names.split())
# # names_list = print(result)

# # # # # # 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# # # # # # 'Chicago']. Convert this list into a single string where each city is separated by a 
# # # # # # semicolon and a space. Store the result in a string called cities_string.
# # cities_list = ['New York', 'Los Angeles', 'Chicago']
# # cities_string = "; ".join(cities_list)
# # print(cities_string)

# # # # # 19.	Create a string variable sentence with the value "the quick brown fox jumps over the 
# # # # # lazy dog". Capitalize the first letter of the string and 
# # # # # print the result.
# # sentence = "the quick brown fox jumps over the lazy dog"
# # print(sentence.capitalize())

# # # # # 20. 	Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# # # # # the first letter of each word and print the result.
# # book_title = "to kill a mockingbird"
# # print(book_title.title())

# # # # # 21. 	Create a string variable text with the value "hello world". Count the number of 
# # # # # occurrences of the letter 'o' and print the result.
# # text = "hello world"
# # print(text.count("o"))

# # # # # 22. 	Create a string variable filename with the value "document.txt". Check if the string 
# # # # # starts with "doc" and print the result.
# # filename = "document.txt"
# # print(filename.startswith("doc"))

# # # # # 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# # # # # string ends with ".com" and print the result.
# # url = "https://www.example.com"
# # print(url.endswith(".com"))

# # # # # 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# # # # # the position of the word "needle" and print the result.
# # phrase = "find the needle in the haystack"
# # print(phrase.find("needle"))

# # # # # 25.	Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# # # # # format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# # # # # Result. Bonus point if you can do it with the f-string and concatenation methods also.
# # name = "Alice" 
# # place = "Wonderland"
# # template = "Hello, {}. Welcome to {}."
# # print(template .format(name, place))
# # template = f"Hello, {name}. Welcome to {place}."
# # print(template)
# # template = "Hello, " + name + ". Welcome to " + place + "."
# # print(template) 

# # # # # 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# # # # # of the word "not" and print the result.
# # quote = "To be or not to be"
# # print(quote.find("not"))

# # # # # 27.	Create a string variable word with the value "hello". Check if all characters in the 
# # # # # string are lowercase and print the result.
# # word = "hello"
# # print(word.islower())

# # # # # 28.	Create a string variable shout with the value "HELLO". Check if all characters in the 
# # # # # string are uppercase and print the result.
# # shout = "HELLO"
# # print(shout.isupper())

# # # # 29.	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# # # # lowercase and print the result.
# # mixed_case = "PyThOn"
# # print(mixed_case.lower())

# # # # 30. 	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# # # # uppercase and print the result.
# # mixed_case = "PyThOn"
# # print(mixed_case.upper())

# # # # 31. 	Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# # # # print the result.
# # padded_text = " hello "
# # print(padded_text.lstrip())

# # # # 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# # # # print the result.
# # padded_text = " hello "
# # print(padded_text.rstrip())

# # # # 33.	Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# # # # whitespace and print the result.
# # padded_text = " hello "
# # print(padded_text.strip())

# # # # 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# # # # and print the result.
# # greeting = "Hello, World!"
# # print(greeting.replace("World", "Alice"))

# # # 2nd assignment

# # # 1. Write a program that asks the user for their name and then greets them with their 
# # # name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# # name = input("What is your name? ")
# # print(f"Hello {name}")

# # # 2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# # # format “You are {age} years old.”.
# # birth_year = input("When were you born? ")
# # age = 2026 - int(birth_year)
# # print(f"You are {age} years old")

# # # 3. Ask the user for their favourite color. Print a statement that includes the color in 
# # # the format “Your favorite color is {favourite_color}.”.
# # favourite_color = input("What is your favourite color? ")
# # print(f"Your favourite color is {favourite_color}")

# # # 4. Ask the user to input some text and check if it is a palindrome. A palindrome is a 
# # # word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or 
# # #  `nurses run` or `121`.
# # # Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. 
# # #  `is_palindrome` is either `True` or `False`.
# # text = input("Write a palindrome or not: ")
# # is_palindrome = text == text[::-1]
# # print(f"It is {is_palindrome} that {text} is a palindrome.")

# # # 5. Create a program that asks the user to input a password and checks if it meets certain 
# # # criteria (at least 8 characters and not more than 30 characters).
# # # Print a statement in the format “It is {is_valid} that the password fulfils the 
# # # criteria.”. `is_valid` is either `True` or `False`.
# # # Bonus point if you can hide the password input from displaying on the screen as clear text.
# # from getpass import getpass
# # password = getpass("Input password: ")
# # print(len(password))
# # criteria = len(password) >= 8 and len(password) <= 30
# # is_valid = password = criteria == True
# # print(f"It is {is_valid} that the password fulfils the criteria.")

# # # 6. Write a program that asks the user for their weight (in kilograms) and height (in 
# # # meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula 
# # # BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in 
# # # the format “Your BMI is {BMI}”.
# # weight = float(input("What is your weight?(in kilograms) "))
# # height = float(input("What is your height?(in meters) "))
# # BMI = round(weight / (height ** 2), 2)
# # print(f"Your BMI is {BMI}")

# # # ---------------------------------------------------ASSIGNMENT---------------------------------------------------

# # 1) Find total cost.
# # Input: price_per_item = 19, quantity = 3
# # Output: 57
price_per_item = 19
quantity = 3
print(price_per_item * 3)

# # # 2) Get average of two scores (show result as a number).
# # # Input: score1 = 78, score2 = 86
# # # Output: 82.0
score1 = 78
score2 = 86
average = (score1 + score2) / 2
print(average) 

# # # 3)How many full boxes are needed given items and box capacity.
# # # Input: items = 53, box_capacity = 6
# # # Output (full boxes): 8
items = 53 
box_capacity = 6
full_boxes = items // box_capacity
print(f"(full_boxes): {full_boxes}")

# # # 4) How many items left over after filling full boxes.
# # # Input: items = 53, box_capacity = 6
# # # Output (leftover items): 5
items = 53
box_capacity = 6
leftover = items % box_capacity
print(f"(leftover items): {leftover}")

# # 5) Test evenness.
# # Input: n = 42
# # Output: True # (True if n is even, False if odd)
# print(4 % 2)
n = 43
# test_even = n % 2 = 0
is_even = n % 2 == 0
print(is_even)

# # 6) Compute the cube of a number.
# # Input: x = 4
# # Output: 64
x = 4
print(x ** 3)

# # 7) Temperature conversion (Celsius to Fahrenheit).
# # Input: celsius = 25
# # Output: 77.0
celsius = 25
conversion = (celsius * (9/5)) + 32
print(conversion)

# # 8) Currency to smallest unit: convert dollars to cents.
# # Input: dollars = 3.25
# # Output: 325
dollars = 3.25
cents = dollars * 100
print(cents)

# # 9) Time conversion: given total seconds, compute minutes and remaining seconds.
# # Input: total_seconds = 125
# # Output: 2 minutes and 5 seconds
total_seconds = 125
minutes = total_seconds // 60
remaining = total_seconds % 60
print(f"{minutes} minutes and {remaining} seconds")

# # 10) Check if a number is strictly between two others.
# # Input: low = 10, x = 14, high = 20
# # Output: True
low = 10
x = 14
high = 20
is_in_range = low < x < high
print(is_in_range)

# # 11) Is the number divisible by both 3 and 5?
# # Input: n = 30
# # Output: True
n = 30
with_decimal = n / 3 and n / 5 
without_decimal = n % 3 == 0 and n % 5 == 0
is_divisible = with_decimal == without_decimal
print(is_divisible)

# # 12) Extract the last digit of a positive integer.
# # Input: n = 12345
# # Output: 5
n = 12345
print(n % 10)

# # 13) Compare two integers and print if they are equal (True/False).
# # Input: a = 42, b = 42
# # # Output: True
a = 42
b = 42
are_equal = a == b
print(are_equal)

# # # 14) Compute the midpoint (average) between two integers.
# # # Input: p = 5, q = 8
# # # Output: 6.5
p = 5
q = 8
average = (q + p) / 2
print(average)

# # # 15) Compute cost per person: total_bill divided equally among people (show decimal if needed).
# # # Input: total_bill = 123.45, people = 4
# # # Output: 30.8625
total_bill = 123.45
people = 4
cost_per_person = total_bill / people
print(cost_per_person)

# # # 16) Convert a price given in euros to another currency using a rate.
# # # Input: euros = 50, rate = 1.13
# # # Output: 56.5
euros = 50
rate = 1.13
new_currency = round(euros * rate, 2)
print(new_currency)

# # # 17) Show the opposite of a given boolean value.
# # # Input: flag = False
# # # Output: True
flag = False
print(not flag)

# # ---------------------------------------------------ASSIGNMENT---------------------------------------------------