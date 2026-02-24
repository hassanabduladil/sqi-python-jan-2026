"""A module to teach students functions"""

# def is_strong_password(password):

#     is_at_least_8_chars_long = len(password) >= 8

#     has_upper = any(char.isupper() for char in password)
#     has_lower = any(char.islower() for char in password)

#     return is_at_least_8_chars_long and has_upper and has_lower


# password1 = "p@ssw0rd123"

# password2 = "p@ssword"

# password3 = "p@Ssword123"

# print(is_strong_password(password1))
# print(is_strong_password(password2))
# print(is_strong_password(password3))


# def greet():
#     print("Heyyy")


# print("Lovely to meet you!")

# greet()

# print("Good morning")





# print("Lorem ipsum dolor")  # 1

# def greet():
#     print("sit amet")  # 3, 6
#     print('Hello World!')  # 4, 7

# print('tempor incididunt ut labore')  # 2
# greet()
# print("consectetur adipiscing elit")  # 5
# greet()
# print("Nemo enim ipsam voluptatem")  # 8




# print("The sun rises in the east")  # 1


# def greet():
#     print("How's it going?")  # 2, 5, 7, 10
#     print("Stay curious, stay kind.")  # 3, 6, 8, 11


# greet()

# print("Midnight thoughts and coffee sips")  # 4
# greet()
# greet()
# print("Learning never exhausts the mind")  # 9
# greet()
# print("Wander often, wonder always")  # 12


# function name is 'talk'
# function should print 'I am talking' when you call it


# def talk():
#     print("I am talking")


# talk()


# def square(num):
#     print(num ** 2)

# square(12)
# number = 100
# square(number)
# num = int(input("Enter a number: "))
# square(num)


# def square():
#     num = int(input("Enter a number: "))

#     print(num ** 2)

# square()


# def name_to_upper(name):
#     print(name.upper())

# name_to_upper("Winnie")


# def add_nums(num1, num2):
#     print(num1 + num2)

# add_nums(4, 10)



# raise_to_power(base, exponent)


# raise_to_power(5, 3)



# Write a function `add_two_nums` that takes in two separate numbers a and b and returns the result of adding them
# Print what it returns.


# def raise_to_power(base, exponent):
#     return base ** exponent

# result = raise_to_power(7, 2)
# print(result)

# print(raise_to_power(4, 5))


# Write a function called `all_except_lagos` which takes in a list of states `["Abuja", "Imo", "Jigawa", "Lagos", "Kogi"]` and returns a list of all the states except Lagos.
# Call the function and print what it returns.


def all_except_lagos(states):
    states_except_lagos = []
    for state in states:
        if state != "Lagos":
            states_except_lagos.append(state)
    return states_except_lagos


# print(all_except_lagos(["Abuja", "Imo", "Jigawa", "Lagos", "Kogi"]))


# def all_except_lagos(states):
#     return [state for state in states if state != "Lagos"]


# print(all_except_lagos(["Abuja", "Imo", "Jigawa", "Lagos", "Kogi"]))


# def turn_states_to_upper(states):
#     return [state.upper() for state in states]

# states_except_lagos = all_except_lagos(["Abuja", "Imo", "Jigawa", "Lagos", "Kogi"])
# print(states_except_lagos)

# # print(turn_states_to_upper(states_except_lagos))
# states_except_lagos_upper = turn_states_to_upper(states_except_lagos)
# print(states_except_lagos_upper)


# def turn_states_to_upper(states: list[str]):  # type hint / annotation
#     states = all_except_lagos(states)
#     return [state.upper() for state in states]


# print(turn_states_to_upper(["Abuja", "Imo", "Jigawa", "Lagos", "Kogi"]))



# Aermeans
# def say_hi_to_everyone(names_and_emojis: dict[str, str]):
#     for name, emoji in names_and_emojis.items():
#         print(f"Hi {name} {emoji}")


# say_hi_to_everyone({"Winnie": "👀", "Olumide": "🫡", "Francis": "😀", "Pelumi": "💰"})


# 4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# # For example, if the string is "beautiful", the result would be 5.


# def count_vowels(text: str):
#     no_of_vowels = 0

#     vowels = "aeiou"

#     for char in text:
#         if char.lower() in vowels:
#             no_of_vowels += 1

#     return no_of_vowels

# print(count_vowels("beautiful"))


# def count_vowels(text: str):
#     return sum(char in "aeiou" for char in text)

# print(count_vowels("beuatiful"))




# -----------------------------------------ASSIGNMENT CORRECTION 1-----------------------------------------------
# 1. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# after, print the result of the function.
# For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]



# 2. Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys "first", "middle", and "last".
# The function should return only the middle name.
# For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"}, then the result would be "James". Another example is if name_dict is {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".


# def get_middle_name(name_dict: dict[str, str]):
#     return name_dict["middle"]

# def get_middle_name(name_dict: dict[str, str]):
#     if "middle" in name_dict:
#         return name_dict["middle"]


# def get_middle_name(name_dict: dict[str, str]):
#     return name_dict.get("middle")


# print(get_middle_name({"first": "Tola", "middle": "James", "last": "Akin"}))
# print(get_middle_name({"middle": "Chioma", "first": "Ada", "last": "Okeke"}))
# print(get_middle_name({"first": "Ada", "last": "Okeke"}))


# 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# For example, if the string is "Python", the result would be "nohtyP".


# 4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# For example, if the string is "beautiful", the result would be 5.

# 5. Create a function called even_numbers that takes in a list of integers and returns a new list containing only the even numbers.
# For example, if the list is [1, 2, 3, 4, 5, 6], the result would be [2, 4, 6].

# 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# For example, if the list is [12, 45, 3, 67, 23], the result would be 67.

# 7. Create a function called sum_dict_values that takes in a dictionary with numeric values and returns the sum of all the values.
# For example, if the dictionary is {"a": 10, "b": 20, "c": 5}, the result would be 35.

# 8. Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# For example, if the list is ["apple", "banana", "cherry"], the result would be {"apple": 5, "banana": 6, "cherry": 6}.

# def word_lengths(words: list[str]):
#     return {word: len(word) for word in words}

# print(word_lengths(["apple", "banana", "cherry"]))
# print(word_lengths([]))


# 9. Create a function called is_palindrome that takes in a string and returns True if the string is a palindrome (same forwards and backwards), otherwise False.
# For example, if the string is "level", the result would be True. If the string is "hello", the result would be False.

# def is_palindrome(text: str):
#     text = text.lower().replace(" ", "")
#     return text == text[::-1]
    

# print(is_palindrome("tenet"))
# print(is_palindrome("nurses run"))

# 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# For example, if list1 = [1, 2, 3] and list2 = [3, 4, 5], the result would be [1, 2, 3, 4, 5].

# def merge_lists(list1: list[int], list2: list[int]):
#     unique_nums = []
#     combined_list = list1 + list2
#     for num in combined_list:
#         if num not in unique_nums:
#             unique_nums.append(num)
#     return unique_nums

# print(merge_lists([1, 2, 3], [3, 4, 5]))

# def merge_lists(list1: list[int], list2: list[int]):
#     unique_nums = []
#     combined_list = [*list1, *list2]
#     for num in combined_list:
#         if num not in unique_nums:
#             unique_nums.append(num)
#     return unique_nums
# print(merge_lists([1, 2, 3], [3, 4, 5]))




# -----------------------------------------ASSIGNMENT CORRECTION 1-----------------------------------------------


# -----------------------------------------ASSIGNMENT CORRECTION 2-----------------------------------------------


# Write a function sum_numbers(a, b) that returns the sum of two numbers.
# Write a function is_even(n) that returns True if n is even and False if n is odd.
# Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False
# Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
# Write a function vol(radius) that computes the volume of a sphere given its radius.
# Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
# Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
# 13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# Sample List: [1, 2, 3, -4]
# Expected output: -24
# 14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# least once. For example: “The quick brown fox jumps over the lazy dog”.
# Hint: Import and use the string module.
# 15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# other. a word, phrase, or name formed by rearranging the letters of another, such as
# spar, formed from rasp.
# 16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# (BMI) given weight in kilograms and height in meters.
# 17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# simple interest given principal amount, interest rate, and time (in years).



# -----------------------------------------ASSIGNMENT CORRECTION 2-----------------------------------------------



# -----------------------------------------*ARGS AND **KWARGS-----------------------------------------------


# def greet(name, time_of_day):
#     return f"Good {time_of_day}, {name}"

# print(greet("Winnie", "morning"))
# print(greet("morning", "Winnie"))
# print(greet(time_of_day="morning", name="Winnie"))


# def greet(time_of_day="morning", name="James"):
#     return f"Good {time_of_day}, {name}"

# print(greet("Winnie", "afternoon"))
# print(greet())
# print(greet(name="Jake"))

# def add_numbers(num1, num2, num3, num4, num5):
#     return num1 + num2 + num3 + num4 + num5

# print(add_numbers(4, 9, 10, 2, 7))



# def add_numbers(*nums):
#     return sum(nums)


# print(add_numbers())


# def greet_all(*names):
#     for name in names:
#         print(f"Hi {name}")

# greet_all("James", "Jake", "Jill", "Janet")



def states_and_capitals(**states_and_their_capitals):
    print(states_and_their_capitals)
    print(type(states_and_their_capitals))
    for state, capital in states_and_their_capitals.items():
        print(f"The Capital of {state} is {capital}")


# states_and_capitals(osun="Osogbo", oyo="Ibadan", ondo="Akure")
# states_and_capitals(**{'osun': 'Osogbo', 'oyo': 'Ibadan', 'ondo': 'Akure'})



# my_dict = {'os un': 'Osogbo', 'oyo': 'Ibadan', 'ondo': 'Akure'}

# my_dict.update()


# print("Hello", "hi", "dbejf", "yegfhijekfl", sep="*")


# ====================================ASSIGNMENT===========================================
# 1. Create a function called get_total_length that returns the total number of characters in all the words passed in.

# Test Data:
# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))

# Expected Output:
# 14
# 7

# def get_total_length(*words):
#     return sum(len(word) for word in words)

# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))

# 2. Create a function called highest_score that returns the name of the student with the highest score.


# def highest_score(**students_with_scores):
#     # return max(students_with_scores, key=students_with_scores.get)
#     return max(students_with_scores.values())

# # Test Data:
# print(highest_score(Ada=72, Bisi=89, Charles=67))
# print(highest_score(Emeka=90, Zainab=88, Tolu=91))

# Expected Output:
# Bisi
# Tolu



# -----------------------------------------*ARGS AND **KWARGS-----------------------------------------------



# -----------------------------------------RECURSION-----------------------------------------------

# def power(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call


# print(power(2, 3))  # Output: 8
# 2 * power(2, 2)
# 2 * 2 * power(2, 1)
# 2 * 2 * 2 * power(2, 0)
# 2 * 2 * 2 * 1 -> 8


# -----------------------------------------RECURSION-----------------------------------------------



# -----------------------------------------SCOPE-----------------------------------------------


# def my_func(text_passed_to_func):
#     global global_var
#     global_var = "Global Var Updated"
#     print(global_var)
#     text_in_func = "Hello"  # local
#     print(text_passed_to_func)
#     print(text_in_func)

# global_var = "Global Var"
# my_func("something")
# print(global_var)
# print(text_passed_to_func)
# print(text_in_func)  # global scope



# def add_two_nums(a, b):
#     """
#     Add two nums
#     a: int
#     b: int
#     Returns a + b
#     """
#     print("Adding the numbers...")
#     return a + b

# print(add_two_nums(8, 2))

# print(help(add_two_nums))

# -----------------------------------------SCOPE-----------------------------------------------


# Write a function multiply(list_items) to multiply all the numbers in a list.
# Sample List: [1, 2, 3, -4]
# Expected output: -24

# def multiply(list_items):
#     result = 1
#     for item in list_items:
#         # result *= item
#         result = result * item

#     return result

# print(multiply([1, 2, 3, -4, 8]))

# Create a function called multiply_first_two that returns the product of the first two numbers passed in.

# def multiply_first_two(*numbers):
#     return numbers[0] * numbers[1]



# # Test Data:
# print(multiply_first_two(3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))

# Expected Output:
# 15
# 20


