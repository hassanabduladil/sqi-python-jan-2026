# # CONDITIONAL STATEMENTS



# # num = input("Enter a number: ")
# # if int(num) % 2 == 0:
# #     print(f"{num} is even")
# # else:
# #     print(f"{num} is odd")


# # name = input("What is your name? ")
# # if name.lower().endswith("a"):
# #     print("Your name ends with a")
# # else:
# #     print("your name does not end with a")


# # temp = int(input("Enter a temperature: "))
# # if temp < 30:
# #     print("It is freezing")
# # elif 31 <= temp <= 100:
# #     print("The temperature is ok")
# # else:
# #     print("The weather is hot")


# # has_umbrella = True
# # has_raincoat = False
# # if has_umbrella and has_raincoat:
# #     print("You have double protection from the rain")
# # elif has_umbrella or has_raincoat:
# #     print("You are protected from the rain")
# # else:
# #     print("You are not protected from the rain")



# # score = int(input("What did you score? "))
# # if 90 <= score <= 100:
# #     print("A")
# # elif 80 <= score <= 89:
# #     print("B")
# # elif 70 <= score <= 79:
# #     print("C")
# # elif 60 <= score <= 69:
# #     print("D")
# # elif 0 <= score < 60:
# #     print("F")
# # else:
# #     print("It has to be greater than or equal to 0 and below or equal to 100")



# # mode = input("Enter the mode: ").lower().strip()
# # if mode == "manual":
# #     print("Manual mode activated")
# # elif mode == "automatic":
# #     print("Automatic mode activated")
# # elif mode == "off":
# #     print("System is off")
# # else:
# #     print("Invalid mode entered.")



# # MONDAY ASSIGNMENT


# # 1. Collect two numbers as input from the user and assign as variables, a and b, write an if statement
# # that prints "a and b are both positive" if both a and b are positive, 
# # prints "Only one is positive" if one of them is positive, and prints "Neither 
# # is positive" if neither is positive.

# # a = int(input("Enter a number: "))
# # b = int(input("Enter another number: "))
# # if a > 0 and b > 0:
# #     print(f"{a} and {b} are positive")
# # elif a > 0 or b > 0:
# #     print(f"Only one is positive")
# # else:
# #     print("Neither is positive")


# # 2. Collect three numbers x, y and z as a comma separated string input from the user and print 
# # "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in 
# # STRICTLY decreasing order, and "Neither" otherwise.  

# # x, y, z = input("Enter three numbers: ").split()
# # if x < y < z:
# #     print("Increasing order")
# # elif x > y > z:
# #     print("Decreasing order")
# # else:
# #     print("Neither") 


# # 3. Write a program that reads a string called `palindrome` supplied through user input and checks if 
# # it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".

# # palindrome = input("Enter a palindrome: ").lower().strip()
# # if not palindrome:
# #     print("Invalid Entry")
# # elif palindrome == palindrome[::-1]:
# #     print("Is a palindrome")
# # else:
# #     print("Not a palindrome")


# # 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if 
# # statement that checks if exactly two out of the three variables are equal and prints "Two are equal" 
# # if this is true. Otherwise, print "All different" or "All same" accordingly.

# # x = int(input("Enter a number: "))
# # y = int(input("Enter another number: "))
# # z = int(input("Enter another number: "))
# # if x == y == z:
# #     print("All same")
# # elif x == y or x == z or y == z:
# #     print("Two are equal")
# # else:
# #     print("All different")



# # 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use 
# # if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the 
# # angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".

# # angle1 = int(input("Enter the first angle: ")) 
# # angle2 = int(input("Enter the second angle: ")) 
# # angle3 = int(input("Enter the third angle: "))
# # # if angle1 > 0 and angle2 > 0 and angle3 > 0:
# # if angle1 + angle2 + angle3 and (angle1 > 0 and angle2 > 0 and angle3 > 0) == 180:
# #     print("Valid triangle")
# # else: 
# #     print("Invalid triangle")


# # 6. You have a single character variable `ch` supplied through user input. Write an if statement 
# # that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and 
# # "Consonant" otherwise. Assume that the input is a single alphabet character.

# # ch = input("Enter a character: ").lower().strip()
# # if ch.startswith(("a", "e", "i", "o", "u")):
# #     print("Vowel")
# # elif ch.startswith(("a", "b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y","z")):
# #     print("Consonant")
# # else:
# #     print("Invalid")


# # 7. Given a comma separated string input from the user of three colors color1, color2, and color3, 
# # write an if statement to check if all three colors are primary colors (red, blue, yellow). Print 
# # "All primary colors" if they are, otherwise print "Not all primary colors".
# # [color1, color2, color3] = input("Enter a color: ").join()
# # colors = [color1, color2, color3]
# # if colors == ["red", "blue", "yellow"]:
# #     print("All primary colors")
# # else:
# #     print("Not all primary colors")



# # 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". 
# # Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic 
# # mode activated" if mode is "automatic", and "System is off" if mode is "off".

# # mode = input("Enter the mode: ").lower().strip()
# # if mode == "manual":
# #     print("Manual mode activated")
# # elif mode == "automatic":
# #     print("Automatic mode activated")
# # elif mode == "off":
# #     print("System is off")
# # else:
# #     print("Invalid mode entered.")


# # 9. Given a string `message` entered by the user, use if statements to check if the message contains 
# # any of the words "urgent", "important", or "immediate". If it contains any of these words, 
# # print "High priority message". Otherwise, print "Normal message".

# # message = input("Enter a message: ").lower().strip()
# # if "urgent" in message or "important" in message or "immediate" in message:
# #     print("High priority message")
# # else:
# #     print("Normal Message") 


# # 10.	You have two variables, status1 and status2, provided through user input, each of 
# # 	which can be "active", “inactive", or "pending". Write an if statement to print 
# # 	"Both active" if both statuses are "active", "One active" if exactly one is "active",
# # 	and "None active" if neither is "active".

# # status1 = input("What is your status: ").lower().strip()
# # status2 = input("What is your other status: ")
# # if status1 == "active" and status2 == "active":
# #     print("Both active")
# # elif status1 == "active" or status2 == "active":
# #     print("One active")
# # else:
# #     print("None active")


# #  11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# # 	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# # 	print "Not an image file".

# # filename = input("Enter your filename: ").lower().strip()
# # if filename.endswith((".jpg", ".png", ".gif")):
# #     print("Image file")
# # else:
# #     print("Not an image file")


# #  12. 	You have a variable `access_level` provided through user input which can be "admin",
# # 	"user", or "guest". Write an if statement that prints "Full access" if access_level is
# # 	"admin", "Limited access" if it is "user", and "No access" if it is "guest".

# # access_level = input("Enter your level: ").lower().strip()
# # if access_level == "admin":
# #     print("Full access")
# # elif access_level == "user":
# #     print("Limited access")
# # elif access_level == "guest":
# #     print("No access")
# # else:
# #     print("Invalid mode")


# #  13. 	Given a string `email` collected from the user, write an if statement to check if the
# # 	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# # 	print "Invalid email".

# # email = input("Enter your email address: ").lower().strip()
# # if "@" in email and "." in email:
# #     print("Valid email")
# # else: 
# #     print("Invalid email")



# #  14. 	You have a variable `day` provided by user input which can be any day of the week 
# # 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# # 	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

# # day = input("Enter a day of the week: ").lower().strip()
# # if day == "saturday" or day == "sunday":
# #     print("Weekend")
# # else:
# #     print("Weekday")


# #  15. 	Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# 	# input from the user and prints the greatest number. Use conditional statements
# 	# to determine which number is the greatest. Bonus point if you can do it without `else` 
# 	# statements.
# num1, num2, num3 = input("Enter 3 numbers seperated by a comma: ").split(", ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
# if num1 > num2 > num3:
#     print(num1)
# elif num1 < num2 and num2 > num3:
#     print(num2)
# elif num1 > num2 and num2 < num3:
#     print(num3)
# elif num1 < num2 < num3:
#     print(num3)



# # Exercise 1
# # An amusement park ride has these rules:
# # - Must be at least 120 cm tall to ride.
# # - If under 120 cm but with an adult, still allowed.
# # - Otherwise, not allowed.
# #
# # Example input/output executions:
# #
# # Enter height: 130
# # With adult? no
# # Output: Allowed
# #
# # Enter height: 110
# # With adult? yes
# # Output: Allowed
# #
# # Enter height: 110
# # With adult? no
# # Output: Not allowed
# #
# # Enter height: 119
# # With adult? yes
# # Output: Allowed
# #
# # Enter height: 100
# # With adult? no
# # Output: Not allowed
# #
# # Enter height: 150
# # With adult? no
# # Output: Allowed

# # height = int(input("Enter your height in centimeters: "))
# # with_adult = input("Are you with an adult? ").lower().strip()
# # if 0 <= height >= 120:
# #     print("Allowed")
# # elif with_adult == "yes":
# #     print("Allowed")
# # else: 
# #     print("Not allowed")


# # Exercise 2
# # An exam grading system with retake rule:
# # The user enters exam score and retake status ("yes" or "no").
# # - If score is at least 50, print "Pass".
# # - If score is less than 50 but retake is "yes", print "Retake allowed".
# # - If score is less than 50 and no retake, print "Fail".
# #
# # Example input/output executions:
# #
# # Enter score: 42
# # Retake? yes
# # Output: Retake allowed
# #
# # Enter score: 42
# # Retake? no
# # Output: Fail
# #
# # Enter score: 50
# # Retake? no
# # Output: Pass
# #
# # Enter score: 75
# # Retake? yes
# # Output: Pass
# #
# # Enter score: 10
# # Retake? no
# # Output: Fail


# # at_least_50 = 0 <= int(input("Enter your score: ")) < 50
# # # retake = input("Are you retaking the test? ").lower() == "yes"
# # if at_least_50:
# #     retake = input("Are you retaking the test? ").lower() == "yes"
# #     if retake:
# #         print("Retake allowed")
# #     else: 
# #         print("Fail")
# # else:
# #     print("Pass")


# # Exercise 3
# # A ride-hailing app calculates trip approval:
# # The user enters distance (km) and wallet balance.
# # Each km costs 200 units.
# # - If wallet balance is enough for the trip, print "Trip confirmed".
# # - If balance is less but at least half the cost, print "Add funds".
# # - If less than half, print "Trip denied".
# #
# # Example input/output executions:
# #
# # Enter distance: 10
# # Enter wallet balance: 800
# # Output: Trip denied
# # Reasoning: cost = 10 * 200 = 2000; half = 1000; balance = 800.
# # 800 < 1000 (less than half), so "Trip denied".
# #
# # Enter distance: 10
# # Enter wallet balance: 2000
# # Output: Trip confirmed
# # Reasoning: cost = 2000; balance = 2000.
# # balance >= cost, so "Trip confirmed".
# #
# # Enter distance: 10
# # Enter wallet balance: 1000
# # Output: Add funds
# # Reasoning: cost = 2000; half = 1000; balance = 1000.
# # not enough (1000 < 2000) but balance >= half, so "Add funds".
# #
# # Enter distance: 10
# # Enter wallet balance: 400
# # Output: Trip denied
# # Reasoning: cost = 2000; half = 1000; balance = 400.
# # balance < half, so "Trip denied".
# #
# # Enter distance: 5
# # Enter wallet balance: 500
# # Output: Add funds
# # Reasoning: cost = 5 * 200 = 1000; half = 500; balance = 500.
# # not enough (500 < 1000) but exactly half, so "Add funds".


# distance = int(input("Enter the distance in km: "))
# balance = int(input("Enter your wallet balance: "))
# if balance < distance * 200:
#     if balance >= (distance * 200) / 2:
#         print("Add funds")
#     else:
#         print("Trip denied")
# else:
#     print("Trip confirmed")


# # Exercise 4
# # An airport boarding system:
# # The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# # - If both are "yes", print "Proceed to boarding".
# # - If boarding pass is missing, print "No boarding pass".
# # - If passport is missing, print "No passport".
# # - If both missing, print "Denied entry".
# #
# # Example input/output executions:
# #
# # Boarding pass? no
# # Passport? yes
# # Output: No boarding pass
# #
# # Boarding pass? yes
# # Passport? no
# # Output: No passport
# #
# # Boarding pass? no
# # Passport? no
# # Output: Denied entry
# #
# # Boarding pass? yes
# # Passport? yes
# # Output: Proceed to boarding
# #
# # Boarding pass? no
# # Passport? yes
# # Output: No boarding pass

# boarding_pass = input("Do you have a boarding pass? ").lower().strip()
# passport = input("Do you have a passport? ").lower().strip()
# if boarding_pass == "yes" and passport == "yes":
#     print("Proceed to boarding")
# elif boarding_pass == "no" and passport == "yes":
#     print("No boarding pass")
# elif boarding_pass == "yes" and passport == "no":
#     print("No passport")
# else:
#     print("Denied entry")





# AGAIN


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



# SECOND ASSIGNMENT



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

# num1, num2, num3 = input("Enter 3 numbers separated by commas: ").split(", ")

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




# LOOPS

# WHILE LOOPS

# i = 56
# while i <= 70:
#     print(i)
#     i += 1


# i = 32
# while i >= 11:
#     if i % 2 == 0:
#         print(i)
#     i -= 1


# i = 1
# numbers = []
# while i <= 50:
#     i += 1
#     if i <= 50:
#         numbers.join("")
# print(numbers)    



# i = 0
# while i <= 19:
#     i += 1
#     if i % 3 == 0:    
#         if i % 5 == 0:
#             continue  
#         print(i)


# i = 1
# while i <= 30:
#     print(i)
#     i += 1
#     if i == 5 ** 2:
#         break



# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))

# # i = 2
# # print("*" * breadth)
# # while i <= length:
# #     print(breadth * "*")
# #     i += 1

# i = 1
# while i <= breadth:
#     print(length * "*")
#     i += 1


# n = int(input("Enter a number: "))
# sum_of_nums = 0
# i = 1
# while i <= n:
#     sum_of_nums += i
#     i += 1
# print(sum_of_nums)



# WEDNESDAY ASSIGNMENT


# 1ST ASSIGNMENT


# 1. Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# 2. Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello

# i = 1
# while i <= 3:
#     print("Hello")
#     i +=1

# 3. Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10

# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# 4. Print numbers in reverse from 5 to 1 using a while loop.
# Expected Output:
# 5
# 4
# 3
# 2
# 1

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# 5.	Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1

#  6. 	Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#     print("*" * num)
#     i += 1

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****
# 7.	Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****

# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#     print("*" * i)
#     i += 1
    


#  8. 	Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!

# start = int(input("Enter the number to start the countdown from: "))
# while start >= 1:
#     print(start)
#     start -= 1
# else:
#     print("Go!")

#  9. 	Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111


# print("1" * 10)

# 10.  Print a list of the first 12 multiples of 3 starting from 3
# empty = []
# i = 3
# while i <= 12:
#     if i % 3 == 0:
#         empty.append(i)
#     i += 1
# print(empty)



# 2ND ASSIGNMENT


# 1. Write a program that uses a while loop to print numbers from 1 to 10.

# i = 1
# while i <= 10:
#     print(i)
    # i += 1

# 2. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).

# n = int(input("Enter a number: "))
# sum_of_nums = 0
# i = 1
# while i <= n:
#     sum_of_nums += i
#     i += 1
# print(sum_of_nums)


# 5. Write a program that takes an integer input from the user and uses a while loop to print a 
# countdown from that number to zero.

# start = int(input("Enter the number to start the countdown from: "))
# while start >= 1:
#     print(start)
#     start -= 1
# else:
#     print("GO!")


# 6. Write a program that takes an integer n from the user and uses a while loop to print all even 
# numbers from 1 to n.
# n = int(input("Enter a number n: "))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop 
# to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625


# base = int(input("Enter the base: "))
# expo = int(input("Enter the exponent: "))
# result = base ** expo
# i = 1
# while i >= 1:
#     print(f"{base} raised to the power of {expo} is {result}")
#     i -= 1




# THURSDAY


# wild_animals = ("giraffe", "wolf", "snake", "monkey", "lion", "tiger", "cheetah", "elephant", "hyena")
# i = 0
# while i < len(wild_animals):
#     animal = wild_animals[i]
#     print(animal)
#     j = 0
#     while j < len(animal):
#         print(animal[j])
#         j += 1
#     i += 1

# wild_animals = ("giraffe", "wolf", "snake", "monkey", "lion", "tiger", "cheetah", "elephant", "hyena")
# i = 0
# while i < len(wild_animals):
#     if i == "lion":
#         continue    
#     i += 1
# print(wild_animals)


# Ask for the input
# set i to 1 
# since we are goint to 12 while i <= 12
# declare the result to a variable
# print it with f string
# add 1 to i ever loop
# number_to_multiply = int(input("Enter the number for the multiplication table: "))
# i = 1
# while i <= 12:
#     result = number_to_multiply * i
#     print(f"{number_to_multiply} x {i} = {result}")
#     i += 1




# string = input("Enter a string: ")
# 9. Collect a string from the user and use a loop to count the frequency of each character 
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# hippoppotamus

# h - 1
# i - 1
# p - 4
# o - 2
# t - 1
# a - 1

# {'h': 1, 'i': 1, 'p': 4, 'o': 1}


# 1. Have where to store characters and their occurences
# 2. Go through every character in the string
# 3. For each character in the string, if the character is already in the store, then increase its value by 1
# 4. If the character is not already there, add it with a value of 1


# occurences = {}

# text = input("Enter some text: ").strip().lower()

# i = 0

# while i < len(text):
#     char = text[i]
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1
#     i += 1
# print(occurences)


# inventory = {"apples": 4, "oranges": 3, "bananas": 5, "mango": 7}

# inventory["apples"] += 1

# inventory["apples"] = inventory["apples"] + 1


# inventory["citrus"] = 2






# ----------------------------------------------------WEEKEND ASSIGNMENT-----------------------------------------------------------


# ---------------------------------------------1ST ASSIGNMENT------------------------------------------



# 3.  Write a program that takes an integer input from the user and prints the multiplication table for 
# that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# num_to_multiply = int(input("Enter a number for the multiplication table: "))
# i = 1
# while i <= 12:
#     result = num_to_multiply * i
#     print(f"{num_to_multiply} x {i} = {result}")
#     i += 1


# 4. Collect a string from the user and use a loop to reverse the string. Print the reversed string. 
# Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# reverse_word = input("Enter a word or sentence: ").strip()
# i = 1
# arrange = []
# while i <= len(reverse_word):
#     arrange.append(reverse_word[-i])
#     i += 1
# print("".join(arrange))  



# 8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

# n = int(input("Enter a number to get the sum: "))
# i = 1
# sum_of_nums = 0
# while i <= n:
#     if i % 2 == 0:
#         sum_of_nums += i
#     i += 1
# print(sum_of_nums)


#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1

# string = input("Enter a string: ").strip().lower()
# occurence = {}
# i = 0
# while i < len(string):
#     char = string[i]
#     if char in occurence:
#         occurence[char] += 1
#     else:
#         occurence[char] = 1
#     i += 1
# print(occurence)
# occurences = {}


# 10.	Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)

# n = int(input("Enter a number n: "))
# i = 1
# square_of_nums = 0
# while i <= n:
#     square_of_nums += (i ** 2)
#     i += 1
# print(square_of_nums)


#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"

# phrase = input("Enter a phrase: ").strip().lower().split()
# first_letter = []
# i = 0
# while i < len(phrase):
#     first_letter.append(phrase[i][0].upper())
#     i += 1
# print("".join(first_letter))



#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4

# string = input("Enter a string: ").strip()
# i = 0
# while i < len(string):
#     num_of_space = string.count(" ")
#     num_of_words = num_of_space + 1
#     i += 1
# print(num_of_words)

# string = input("Enter a string: ").strip().split()
# i = 0
# words = []
# while i < len(string):
#     words.append(string[i])
#     i += 1
# print(len(words))


#  13. 	Collect a string from the user and only print out the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this Sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence

# string = input("Enter a string: ").split()
# i = 0
# start_with_s = []
# while i < len(string):
#     if string[i].startswith("s"):
#         print(string[i])
#     elif string[i].startswith("S"):
#         print(string[i])
#     i += 1




#  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.

# i = 1
# for i in range(1, 20, 2):
#    print(i)



#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.

# i = 1
# numbers = []
# while i <= 50:
#     if i % 3 == 0:
#         numbers.append(i)
#     i += 1
# print(numbers)




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

# even = input("Enter a sentence: ").split()
# i = 0
# while i < len(even):
#     if len(even[i]) % 2 == 0:
#         print(even[i])
#     i += 1


#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

# i = 1
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     if i % 3 == 0:
#         print("Fizz")
#     if i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
    # i += 1




#  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']
# i = 0
# while i < len(names):
#     print(f"{names[i]} got grade {grades[i]}")
#     i += 1





# 19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

# items = ['shoe', 'stick', 'toy', 'fruit']
# i = 0
# while i < len(items):
#     if i % 2 == 0:
#         print(f"{i}: {items[i]}")
#     i += 1


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

# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]
# i = 0
# differ = []
# while i < len(list1):
#     if list1[i] != list2[i]:
#         differ.append(f"Index {i}: {list1[i]} != {list2[i]}")
#     i += 1
# print(differ)





# 1.
# balance = int(input("Enter your balance: "))

# main_loop = True

# while main_loop:
#     withdrawal_amount = int(input("Enter withdrawal amount: "))

#     if withdrawal_amount > balance:
#         print("Insufficient funds")
#     else:
#         balance -= withdrawal_amount

#         print(f"Remaining balance: {balance}")    

#     while True:

#         another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()

#         if another_withdrawal == "no":
#             print(f"Final balance: {balance}")
#             main_loop = False
#             break
        
#         if another_withdrawal == "yes":
#             break

#         print("You must enter yes/no")

# 2. Write a program that simulates a grocery store checkout. The user should enter the prices of 
# items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48

# cost = 0
# while True:
#     price = float(input("Enter item price: "))
#     cost += price
#     item = input("Enter another item? (yes/no): ").strip().lower()
#     if item == "yes":
#         continue
#     if item == "no":
#         print(f"Total cost: {cost}")
#         break
#     else:
#         print("You have to enter yes/no ")
#         continue 




# 3. Write a program that continuously prompts the user to enter a password until they enter a 
# valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

# while True:
#     password = input("Enter password: ").strip()
#     if 8 <= len(password) <= 25:
#         print("Password accepted")
#         break
#     else:
#         print("Your password must be at least 8 characters long and less than 25 characters")
#         continue




# 4.	Write a program that asks for the user's age and keeps prompting them until they 
# 	enter a valid age (greater than or equal to 0).
# 	Sample Input and Output:
# 	Enter your age: -5
# 	Invalid age. Please enter a valid age.
# 	Enter your age: 25
# 	Age accepted.

# while True:
#     age = int(input("Enter your age: "))
#     if age >= 0:
#         print("Age accepted.")
#         break
#     else:
#         print("Invalid age. Please enter a valid age.")
#         continue


#  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {' eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit

inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam": 2}
while True:
    operation = input("Enter operation (add/remove/exit): ").lower().strip()
    
    if operation == "add":
        item = input("Enter item: ").lower().strip()
        quantity = int(input("Enter quantity: "))
        
        if not item:
            print("Is that our little comedian lol so funny(sarcastic), now enter an actual item")
            continue
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        
        print(inventory)
        continue
    
    if operation == "remove":
        item = input("Enter item: ").lower().strip()
        quantity = int(input("Enter quantity: "))
        
        if not item:
            print("Is that our little comedian, haha so funny(sarcastic), now enter an actual item")
            continue
        if item in inventory:
            inventory[item] -= quantity

            if inventory[item] >= 0:
                print(inventory)
                continue
            else:
                print("You do not have up to that amount in the inventory")
                inventory[item] += quantity
                print(inventory)
                continue
        
        else:
            print("Not in invetory")
        
        print(inventory)
        continue
    
    if operation == "exit":
        break
    else:
        print("You must enter one of add/remove/exit")
        continue