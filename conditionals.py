# weather = "sunny"

# if weather == "sunny":
#     print("Enjoy the weather")
# else:
#     print("Carry an umbrella")



# is_sunny = False

# if is_sunny:
#     print("Enjoy the weather")
# else:
#     print("Carry an umbrella")

# weather = "sunny"

# if weather == "sunny":
#     print("Enjoy the weather")
# elif weather.startswith("s"):
#     print("Beautiful weather today")
# else:
#     print("Must be raining then")


# num1 = 40
# num2 = 34

# if num1 < num2:
#     print(f"{num1} is less than {num2}")
# elif num1 == num2:
#     print(f"{num1} is equal to {num2}")
# else:
#     print(f"{num1} is greater than {num2}")

# 1. Ask the user for a number, and print "{num} is even" if the number is even, otherwise, print "{num} is odd"

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# 2. Ask the user for their name, and if their name endswith the letter "a", print "Your name ends with 'a'". Otherwise, print "Your name does not end with 'a'"


# num = input("Enter a number: ")

# int(num)

# if num.endswith(("0", "2", "4", "6", "8")):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# 3. Ask the user for the temperature.
# If the temperature is less than or equal to 30, print "It is freezing"
# If it is between 31 and 100, "The temperature is ok"
# If it is greater than 101, "The weather is hot!"

# temperature = int(input("Enter the temperature in celcius"))

# if temperature <= 30:
#     print("it is freezing")
# # elif temperature > 30 and temperature <= 100:
# elif 30 < temperature <= 100:
#     print("The temperature is ok")
# else:
#     print("the weather is hot!")



# has_husband = None

# if has_husband is None:
#     print("No husband")
# else:
#     print("Has husband")


# name = input("What is your name? ").strip()

# if name:
#     print(f"Hey {name}!")
# else:
#     print("Hello stranger!")



# name = input("What is your name? ").strip()

# if not name:
#     print("You must enter a name")



# has_umbrella = True
# has_raincoat = True

# # If the person has either an umbrella or a raincoat, print "You are protected from the rain"
# # If they have both an umbrella and a raincoat, "You have double protection from the rain"
# # If they have none of the two, "You are NOT protected from the rain"


# if has_umbrella and has_raincoat:
#     print("You have double protection from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected from the rain")
# else:
#     print("You are NOT protected from the rain")


# name = input("What is your name? ").strip()

# if not name: print("You must enter a name")



# is_male = True

# if is_male:
#     pronoun = "he"
# else:
#     pronoun = "she"

# is_male = True

# pronoun = "he" if is_male else "she"

# print("he") if is_male else print("she")

# print("he" if is_male else "she")


# is_male = True

# age = 1

# if is_male:
#     if age >= 18:
#         print("You are male and are of age to vote")
#     else:
#         print("You are male but not of age")
# else:
#     print("Women cannot vote")


# Ask the user for their score
# and tell them their grade

# "A" - any grade 90-100, inclusive
# "B" - any grade 80-89, inclusive
# "C" - any grade 70-79, inclusive
# "D" - any grade 60-69, inclusive
# "F" - any grade <60

# score = int(input("Enter your score to get your grade: "))

# if 90 <= score <= 100:
#     print("A")
# elif 80 <= score <= 89:
#     print("B")
# elif 70 <= score <= 79:
#     print("C")
# elif 60 <= score <= 69:
#     print("D")
# elif 0 <= score < 60:
#     print("F")
# else:
#     print("Invalid score entered. Enter from 0 to 100")

# # You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".

# mode = input("Enter the mode: ")


# ------------------------------------------ASSIGNMENT CORRECTION------------------------------------------


# Exercise 1
# An amusement park ride has these rules:
# - Must be at least 120 cm tall to ride.
# - If under 120 cm but with an adult, still allowed.
# - Otherwise, not allowed.
#
# Example input/output executions:

# at_least_120 = int(input("Enter height: ")) >= 120
# with_adult = input("With adult? ") == "yes"


# if at_least_120 or with_adult:
#     print("Allowed")
# else:
#     print("Not allowed")

# Enter height: 130
# With adult? no
# Output: Allowed
#
# Enter height: 110
# With adult? yes
# Output: Allowed
#
# Enter height: 110
# With adult? no
# Output: Not allowed
#
# Enter height: 119
# With adult? yes
# Output: Allowed
#
# Enter height: 100
# With adult? no
# Output: Not allowed
#
# Enter height: 150
# With adult? no
# Output: Allowed


# Exercise 2
# An exam grading system with retake rule:
# The user enters exam score and retake status ("yes" or "no").
# - If score is at least 50, print "Pass".
# - If score is less than 50 but retake is "yes", print "Retake allowed".
# - If score is less than 50 and no retake, print "Fail".


# score_at_least_50 = int(input("Enter score: ")) >= 50
# retake_status = input("Retake? ") == "yes"

# if score_at_least_50:
#     print("Pass")
# elif retake_status:
#     print("Retake allowed")
# else:
#     print("Fail")


# Example input/output executions:
#
# Enter score: 42
# Retake? yes
# Output: Retake allowed
#
# Enter score: 42
# Retake? no
# Output: Fail
#
# Enter score: 50
# Retake? no
# Output: Pass
#
# Enter score: 75
# Retake? yes
# Output: Pass
#
# Enter score: 10
# Retake? no
# Output: Fail



# Exercise 3
# A ride-hailing app calculates trip approval:
# The user enters distance (km) and wallet balance.
# Each km costs 200 units.
# - If wallet balance is enough for the trip, print "Trip confirmed".
# - If balance is less but at least half the cost, print "Add funds".
# - If less than half, print "Trip denied".
#

# cost = int(input("Enter distance: ").strip()) * 200
# wallet_balance = int(input("Enter wallet balance: "))
# at_least_half = wallet_balance >= (cost / 2)


# if wallet_balance >= cost:
#     print("Trip confirmed")
# elif at_least_half:
#     print("Add funds")
# else:
#     print("Trip denied")

# Example input/output executions:
#
# Enter distance: 10
# Enter wallet balance: 800
# Output: Trip denied
# Reasoning: cost = 10 * 200 = 2000; half = 1000; balance = 800.
# 800 < 1000 (less than half), so "Trip denied".
#
# Enter distance: 10
# Enter wallet balance: 2000
# Output: Trip confirmed
# Reasoning: cost = 2000; balance = 2000.
# balance >= cost, so "Trip confirmed".
#
# Enter distance: 10
# Enter wallet balance: 1000
# Output: Add funds
# Reasoning: cost = 2000; half = 1000; balance = 1000.
# not enough (1000 < 2000) but balance >= half, so "Add funds".
#
# Enter distance: 10
# Enter wallet balance: 400
# Output: Trip denied
# Reasoning: cost = 2000; half = 1000; balance = 400.
# balance < half, so "Trip denied".
#
# Enter distance: 5
# Enter wallet balance: 500
# Output: Add funds
# Reasoning: cost = 5 * 200 = 1000; half = 500; balance = 500.
# not enough (500 < 1000) but exactly half, so "Add funds".


# Exercise 4
# An airport boarding system:
# The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# - If both are "yes", print "Proceed to boarding".
# - If boarding pass is missing, print "No boarding pass".
# - If passport is missing, print "No passport".
# - If both missing, print "Denied entry".
#
# Example input/output executions:

# has_boarding = input("Boarding pass? ") == "yes"
# has_passport = input("passport pass? ") == "yes"

# if has_boarding and has_passport:
#     print("Proceed to boarding")
# elif not has_passport and not has_boarding:
#     print("Denied entry")
# # elif has_passport:
# elif not has_boarding:
#     print("No boarding pass")
# elif not has_passport:
#     print("no passport")


# Boarding pass? no
# Passport? yes
# Output: No boarding pass
#
# Boarding pass? yes
# Passport? no
# Output: No passport
#
# Boarding pass? no
# Passport? no
# Output: Denied entry
#
# Boarding pass? yes
# Passport? yes
# Output: Proceed to boarding
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass

# ------------------------------------------ASSIGNMENT CORRECTION------------------------------------------



# ------------------------------------------ASSIGNMENT CORRECTION 2------------------------------------------

# 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif a > 0 or b > 0:
#     print("Only one is positive")
# else:
#     print("Neither is positive")


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif a <= 0 and b <= 0:
#     print("Neither is positive")
# else:
#     print("Only one is positive")


# 2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.


# 3. Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".



# 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.

# 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".

# angle1 = float(input("Enter the value of the first angle: "))
# angle2 = float(input("Enter the value of the second angle: "))
# angle3 = float(input("Enter the value of the third angle: "))

# sum_equal_to_180 = (angle1 + angle2 + angle3) == 180

# all_positive = angle1 > 0 and angle2 > 0 and angle3 > 0

# if sum_equal_to_180 and all_positive:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")


# angle1 = float(input("Enter the value of the first angle: "))
# angle2 = float(input("Enter the value of the second angle: "))
# angle3 = float(input("Enter the value of the third angle: "))

# if (angle1 + angle2 + angle3) == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")

#  python gotcha

# 6. You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.

# import string

# lowercase_letters = tuple(string.ascii_lowercase)

# ch = input("Enter a single alphabetic character: ").strip().lower()

# if not ch.startswith(lowercase_letters):
#     print("Not an alphabet")

# elif ch.startswith(("a", "e", "i", "o", "u")):
#     print("Vowel")
# else:
#     print("Consonant")


# 7. Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".

# colors = ("red", "yellow", "blue")

# color1, color2, color3 = input("Enter 3 colors separated by commas: ").lower().split(",")

# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()

# if color1 in colors and color2 in colors and color3 in colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")

# primary_colors = {"red", "yellow", "blue"}

# color1, color2, color3 = input("Enter 3 colors separated by commas: ").lower().split(",")

# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
    
# colors = {color1, color2, color3}

# if colors == primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".

# 9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".

# message = input("Enter a message: ").lower()

# if "urgent" in message or "important" in message or "immediate" in message:
#     print("High priority message")
# else:
#     print("normal message")


# 10.	You have two variables, status1 and status2, provided through user input, each of 
# which can be "active", “inactive", or "pending". Write an if statement to print 
# "Both active" if both statuses are "active", "One active" if exactly one is "active",
# and "None active" if neither is "active".

# 11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# print "Not an image file".

# filename = input("Enter the file name: ").lower().strip()

# if filename.endswith((".jpg", ".png", ".gif")):
#     print("Image file")
# else:
#     print("Not an image file")

# 12. 	You have a variable `access_level` provided through user input which can be "admin",
# "user", or "guest". Write an if statement that prints "Full access" if access_level is
# "admin", "Limited access" if it is "user", and "No access" if it is "guest".

# 13. 	Given a string `email` collected from the user, write an if statement to check if the
# email contains both "@" and "." characters. Print "Valid email" if it does, otherwise
# print "Invalid email".

# email = input("Enter the email address: ")

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")

# 14. 	You have a variable `day` provided by user input which can be any day of the week 
# (e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

# import calendar

# day = input("Enter a day of the week: ").strip().capitalize()
# days_of_the_week = tuple(calendar.day_name)

# weekdays = days_of_the_week[:5]
# weekend = days_of_the_week[-2:]

# if day in weekdays:
#     print("Weekday")
# elif day in weekend:
#     print("Weekend")
# else:
#     print("Not a valid day of the week")

# 15. Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# input from the user and prints the greatest number. Use conditional statements
# to determine which number is the greatest. Bonus point if you can do it without `elif` 
# statements.

# num1, num2, num3 = input("Enter 3 numbers separated by commas: ").split(",")

# num1, num2, num3 = int(num1), int(num2), int(num3)

# if num1 > num2 and num1 > num3:
#     print(f"{num1} is the greatest")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is the greatest")
# elif num3 > num1 and num3 > num2:
#     print(f"{num3} is the greatest")
# else:
#     print("They are all equal")


# num1, num2, num3 = input("Enter 3 numbers separated by commas: ").split(",")

# num1, num2, num3 = int(num1), int(num2), int(num3)

# # 8, 100, 3

# greatest = num1

# if num2 > greatest:
#     greatest = num2

# if num3 > greatest:
#     greatest = num3

# print(f"{greatest} is the greatest")


# ------------------------------------------ASSIGNMENT CORRECTION 2 ------------------------------------------
