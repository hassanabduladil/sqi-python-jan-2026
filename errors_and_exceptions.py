# Examples of Exceptions

# ValueError
# KeyError
# NameError
# TypeError
# AttributeError
# IndexError
# SyntaxError
# IndentationError
# ZeroDivisionError

# print("Hello")




# try...except...else....finally

# try...catch....


# try:
#     num1 = int(input("Enter the value of num1: "))
#     num2 = int(input("Enter the value of num2: "))
#     result = num1 / num2
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("num1 and num2 must be integers")
# except Exception:
#     print("Something went wrong")
# else:
#     print(result)


# ask the user for their age, and tell them their birth year
# if they enter a non-integer, or they enter a negative number, print "Invalid age" and
# keep asking them until they enter a valid age and then show their birth year

# TOCTOU - Time-of-check to time-of-use

# LBYL - Look Before You Leap

# EAFP - Easier to Ask for Forgivenss than Permission

# from datetime import datetime
# current_year = datetime.today().year

# while True:
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError:
#         print("Invalid age")
#     else:
#         if age < 0:
#             print("Invalid age")
#         else:
#             print(f"You were born in {current_year - age}")
#             break

# from datetime import datetime
# current_year = datetime.today().year

# try:
#     age = int(input("Enter your age: "))
# except ValueError as e:
#     print(f"Invalid age: {e}")
# except:
#     print("Something went wrong")
# else:
#     if age < 0:
#         raise ValueError("Invalid age")
#     else:
#         print(f"You were born in {current_year - age}")


# class InvalidAgeError(Exception):
#     def __init__(self, age, *args):
#         super().__init__(*args)
#         self.age = age


# from datetime import datetime
# current_year = datetime.today().year


# def get_birth_year():
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError as e:
#         print(f"Invalid age: {e}")
#     except:
#         print("Something went wrong")
#     else:
#         if age < 0:
#             raise InvalidAgeError(age, "Invalid Age entered")
#         return current_year - age
    

# try:
#     birth_year = get_birth_year()
# except InvalidAgeError as e:
#     print(e)
#     print(e.age)
# else:
#     print(birth_year)


# def main():
#     try:
#         num1 = int(input("Enter the value of num1: "))
#         num2 = int(input("Enter the value of num2: "))
#         result = num1 / num2
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except ValueError:
#         print("num1 and num2 must be integers")
#     except Exception:
#         print("Something went wrong")
#     else:
#         print(result)
#     finally:
#         print("This will always run")



# try:
#     main()
# except KeyboardInterrupt:
#     print("Program interrupted")




# with open("my_file.csv", "r") as f:
#     contents = f.readlines()
    
# header = contents[0]
# contents = contents[1:]

# print(contents)

# for row in contents:
#     cell = row.split(",")
#     parent_item_id, child_item_id, quantity_per, yield_pct, scrap_recovery_pct, effectivity_start, effectivity_end, alternate_bom_id,site_id, is_byproduct, byproduct_credit = cell

#     print(f"Parent Item: {parent_item_id}")
#     print("Site ID: ", site_id)

#     # print(cell)

# with open("my_file.txt", "r") as f:
#     contents = f.readlines()

# with open("processed_data.txt", "w") as f:
#     f.write("Processed data")

# with open("processed_data.txt", "a") as f:
#     f.write("\nThis was appended")



# ----------------------------ASSIGNMENT CORRECTION----------------------------
# 1. Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.

# class NegativeNumberError(Exception):
#     pass

# def check_positive(number):
#     if number < 0:
#         raise NegativeNumberError(f"{number} is negative")
#     return True


# try:
#     print(check_positive(-6))
# except NegativeNumberError as e:
#     print(e)



# 2. Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.

import logging

# def safe_divide(a, b):
#     try:
#         result = int(a) / int(b)
#     except ZeroDivisionError as e:
#         return "Cannot divide by zero"
#     except TypeError as e:
#         return "TypeError: a and b must be integers"
#     except ValueError as e:
#         return "ValueError: a and b must be integers"
#     finally:
#         print("This will always run")
#     return result


# def safe_divide(a, b):
#     try:
#         return int(a) / int(b)
#     except ZeroDivisionError as e:
#         return "Cannot divide by zero"
#     except TypeError as e:
#         return "TypeError: a and b must be integers"
#     except ValueError as e:
#         return "ValueError: a and b must be integers"
#     finally:
#         print("This will always run")


# print(safe_divide(4, "5.8"))
# print(safe_divide(4, [5.8]))
# print(safe_divide(4, 0))


# ----------------------------ASSIGNMENT CORRECTION----------------------------



