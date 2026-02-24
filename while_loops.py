# print("Hy James")
# print("Hy James")
# print("Hy James")
# print("Hy James")
# print("Hy James")
# print("Hy James")
# print("Hy James")
# print("Hy James")
# print("Hy James")
# print("Hy James")

# DRY - Don't Repeat Yourself


# i = 0

# while i < 10:
#     print("Yo James")
#     print(i)
#     i += 1

# i = 10

# while i > 0:
#     print(i)
#     i -= 1


# 1. Count from 56 to 70 i.e. 56, 57, ..., 69, 70

# i = 56

# while i <= 70:
#     print(i)
#     i += 1

# 2. Count down from 32 to 11 showing only the even numbers i.e 32, 30, 28, 26, ..., 14, 12

# i = 32

# while i > 11:
#     print(i)
#     i -= 2

# i = 32

# while i > 11:
#     if i % 2 == 0:
#         print(i)
#     i -= 1


# i = 32

# even_nos = []

# while i > 11:

#     if i % 2 == 0:
#         even_nos.append(i)
#     i -= 1

# print(even_nos)


# 1, 2, 3, ..., 48, 49, 50

# i = 1

# numbers = []

# while i <= 50:
#     numbers.append(str(i))
#     i += 1


# print(", ".join(numbers))


# i = 1

# numbers = ""

# while i <= 50:
#     numbers += str(i)
#     if i != 50:
#         numbers += ", "
#     i += 1


# print(numbers)

# i = 1
# while i <= 50:
#     print(i)
#     if i == 35:
#         break
#     i += 1

# print("End of file")


# i = 0
# while i <= 49:
#     i += 1
#     if i == 35:
#         continue
#     print(i)

# print("End of file")



# 1. Print all the multiples of 3 from 1 to 20, but skip any one that is also a multiple of 5

# i = 0

# while i < 20:
#     i += 1
#     if i % 3 == 0:
#         if i % 5 == 0:
#             continue
#         print(i)

# 2. Print all the numbers from 1 to 30, but stop once you come across the square of 5.

# i = 1

# while i < 30:
#     if i == (5 ** 2):
#         break
#     print(i)
#     i += 1

# i = 1

# while i <= 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# else:
#     print("Condition is false")


# Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


# length = int(input("Enter the length of the square: "))

# i = 1

# while i <= length:
#     print(length * "*")
#     i += 1


# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))

# i = 1

# while i <= breadth:
#     print(length * "*")
#     i += 1



# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).


# n = int(input("Enter the value of n: "))

# sum_of_nums = 0

# i = 1

# while i <= n:
#     sum_of_nums += i
#     i += 1

# print(sum_of_nums)



# --------------------------------------------------------------------ASSIGNMENT CORRECTION -------------------------------------------------------------------------------------

# 8. Print a countdown
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

# number = int(input("Enter the countdown number: "))

# while number >= 1:
#     print(number)
#     number -= 1
# else:
#     print("Go!")



#  9. Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111


# print("1" * 10)

# i = 1

# ones = []

# while i <= 10:
#     ones.append("1")
#     i += 1

# ones = "".join(ones)
# print(ones)

# 10. Print a list of the first 12 multiples of 3 starting from 3

# multiples_of_3 = []
# i = 1
# while len(multiples_of_3) != 12:
#     if i % 3 == 0:
#         multiples_of_3.append(i)
#     i += 1

# print(multiples_of_3)

# multiples_of_3 = []
# i = 1
# while len(multiples_of_3) != 12:
#     multiples_of_3.append(i * 3)
#     i += 1

# print(multiples_of_3)


# i = 1

# multiples_of_3 = []

# while i <= 12:
#     multiples_of_3.append(i * 3)
#     i += 1

# print(multiples_of_3)



# 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
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
# exponent = int(input("Enter the exponent: "))

# # print(base ** exponent)

# i = 1

# result = 1

# while i <= exponent:
#     result = result * base
#     i += 1


# print(f"{base} raised to the power of {exponent} is {result}")

# --------------------------------------------------------------------ASSIGNMENT CORRECTION -------------------------------------------------------------------------------------


# Olumide
# name = "Olumide"

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])

# name = "Olumide"

# i = 0

# # while i <= len(name) - 1:
# while i < len(name):
#     char = name[i]
#     print(char)
#     i += 1

# wild_animals = ("giraffe", "wolf", "snake", "monkey", "lion", "tiger", "cheetah", "elephant", "hyena")

# i = 0

# while i < len(wild_animals):
#     print(wild_animals[i])
#     i += 1

# giraffe
# g
# i
# r
# a
# f
# f
# e
# wolf
# w
# o
# l
# f
# snake
# s
# n
# a
# k
# e
# .
# .
# .


# wild_animals = ("giraffe", "wolf", "snake", "monkey", "lion", "tiger", "cheetah", "elephant", "hyena")

# i = 0

# while i < len(wild_animals):
#     animal = wild_animals[i]
#     print(animal)
#     j = 0
#     while j < len(animal):
#         char = animal[j]
#         print(char)
#         j += 1
#     i += 1



wild_animals = ("giraffe", "wolf", "snake", "monkey", "lion", "tiger", "cheetah", "elephant", "hyena")

# 1. Print all the animals except "lion"

# i = 0

# while i < len(wild_animals):
#     animal = wild_animals[i]
#     i += 1
#     if animal == "lion":
#         continue
#     print(animal)

# 2. Print the animals, but stop AFTER printing "cheetah" i.e. ("giraffe", "wolf", "snake", "monkey", "lion", "tiger", "cheetah")


# i = 0

# while i < len(wild_animals):
#     animal = wild_animals[i]
#     i += 1
#     print(animal)
#     if animal == "cheetah":
#         break


# inventory = {"apples": 4, "oranges": 3, "bananas": 5, "mango": 7}

# inventory = list(inventory.items())

# i = 0

# while i < len(inventory):
#     item_name, item_qty = inventory[i]
#     print(f"{item_name} - {item_qty}")
#     i += 1

# ---------------------------------------------INFINITE WHILE LOOPS---------------------------------------------


# i = 1

# while True:
#     print(i)
#     i += 1


# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350

# balance = int(input("Enter your balance: "))

# while True:
#     withdrawal_amount = int(input("Enter withdrawal amount: "))

#     if withdrawal_amount > balance:
#         print("Insufficient funds")
#     else:
#         balance -= withdrawal_amount

#         print(f"Remaining balance: {balance}")    

#     another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower() == "yes"

#     if not another_withdrawal:
#         print(f"Final balance: {balance}")
#         break


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


# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60



# table_no = int(input("Enter the multiplication table number: "))

# i = 1

# while i <= 12:
#     result = table_no * i
#     print(f"{table_no} X {i} = {result}")
#     i += 1

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


# ---------------------------------------------INFINITE WHILE LOOPS---------------------------------------------



# ---------------------------------------------ASSIGNMENT CORRECTION PART 1---------------------------------------------

# 2. Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48

# total_price = 0

# while True:
#     price = float(input("Enter item price: "))
    
#     total_price += price

#     another_item = input("Enter another item? (yes/no): ").lower() == "yes"

#     if another_item:
#         continue

#     print(f"Total cost: {total_price}")
#     break



# total_price = 0

# main_loop = True

# while main_loop:
#     price = float(input("Enter item price: "))
    
#     total_price += price

#     while True:
#         another_item = input("Enter another item? (yes/no): ").lower()

#         if another_item == "yes":
#             break

#         if another_item == "no":
#             main_loop = False
#             print(f"Total cost: {total_price}")
#             break

#         print("Invalid response, choose between yes/no!")




# 3. Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

# while True:

#     password = input("Enter password: ").strip()

#     is_valid_password = 8 <= len(password) <= 25

#     if is_valid_password:
#         print("Password accepted.")
#         break

#     print("Password must be at least 8 characters long and have a maximum of 25 characters.")


# 4. Write a program that asks for the user's age and keeps prompting them until they 
# enter a valid age (greater than or equal to 0).
# Sample Input and Output:
# Enter your age: -5
# Invalid age. Please enter a valid age.
# Enter your age: 25
# Age accepted.




# 5. Write a program that tracks the inventory of items in a store. The user should be able 
# to add or remove items and the program should display the current inventory after each
# operation. The program stops when the user decides to exit.
# The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# Sample Input and Output:
# Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit

# current_inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam": 2}

# while True:
#     operation = input("Enter operation (add/remove/exit): ").strip().lower()

#     if operation == "exit":
#         print("Good bye")
#         break

#     if operation not in ["add", "remove"]:
#         print("Invalid operation.")
#         continue

#     item = input("Enter item: ").strip().lower()
#     quantity = int(input("Enter quantity: "))

#     if operation == "add":
#         if item in current_inventory:
#             current_inventory[item] += quantity
#         else:
#             current_inventory[item] = quantity
#     elif operation == "remove":
#         if item in current_inventory:
#             if quantity > current_inventory[item]:
#                 print(f"We only have {current_inventory[item]} of {item} in the inventory. {item}'s quantity is now 0")
#                 current_inventory[item] = 0
#             else:
#                 current_inventory[item] -= quantity
#         else:
#             print(f"We do not have {item} in the inventory currently")
#     print(f"Current inventory: {current_inventory}")
        


# ---------------------------------------------ASSIGNMENT CORRECTION PART 1---------------------------------------------



# ---------------------------------------------ASSIGNMENT CORRECTION PART 2---------------------------------------------

# 3, 4, 8, 9, 10, 11

# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.

# from random import randint

# secret_number = randint(1, 50)

# attempts = 5

# while attempts >= 1:
#     guess = int(input("Guess the secret number between 1 and 50: "))

#     if not(1 <= guess <= 50):
#         print("Invalid guess. It must be between 1 and 50")
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




# ---------------------------------------------ASSIGNMENT CORRECTION PART 2---------------------------------------------