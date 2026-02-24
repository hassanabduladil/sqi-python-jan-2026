# # ----------------------------------------------FUNCTIONS-------------------------------------------------

# # ASSIGNMENT

# # -------------------------
# # EXERCISE 1
# # -------------------------
# # Create a function called greet()
# # It should print: Hello there!
# #
# # Expected output:
# # Hello there!
# #
# # Function call:
# # greet()


# # def greet():
# #     print("Hello there!")

# # greet()




# # -------------------------
# # EXERCISE 2
# # -------------------------
# # Create a function called say_name(name)
# # It should print the name in all caps
# #
# # Expected output:
# # JOHN
# #
# # Function call:
# # say_name("John")

# # def say_name(name):
# #     print(name.upper())

# # say_name("John")



# # -------------------------
# # EXERCISE 3
# # -------------------------
# # Create a function called show_age(age)
# # It should print: You are <age> years old
# #
# # Expected output:
# # You are 15 years old
# #
# # Function call:
# # show_age(15)

# # def show_age(age):
# #     print(f"You are {age} years old")

# # show_age(15)



# # -------------------------
# # EXERCISE 4
# # -------------------------
# # Create a function called multiply_by_two(num)
# # It should print the number multiplied by 2
# #
# # Expected output:
# # 20
# #
# # Function call:
# # multiply_by_two(10)

# # def multiply_by_two(num):
# #     print(num * 2)

# # multiply_by_two(10) 


# # -------------------------
# # EXERCISE 5
# # -------------------------
# # Create a function called subtract_numbers(a, b)
# # It should print the result of a - b
# #
# # Expected output:
# # 7
# #
# # Function call:
# # subtract_numbers(10, 3)

# # def subtract_numbers(a, b):
# #     print(a - b)

# # subtract_numbers(10, 3)


# # -------------------------
# # EXERCISE 6
# # -------------------------
# # Create a function called ask_and_square()
# # The function should:
# # - Ask the user to enter a number
# # - Print the square of that number
# #
# # Expected input:
# # 4
# #
# # Expected output:
# # 16
# #
# # Function call:
# # ask_and_square()

# # def ask_and_square():
# #     num_to_square = int(input("Enter a number to square: "))
# #     print(num_to_square ** 2)

# # ask_and_square()


# # -------------------------
# # EXERCISE 7
# # -------------------------
# # Create a function called print_length(word)
# # It should print the length of the word
# #
# # Expected output:
# # 6
# #
# # Function call:
# # print_length("Python")

# # def print_length(word):
# #     print(len(word.strip()))

# # print_length("Python")


# # -------------------------
# # EXERCISE 8
# # -------------------------
# # Create a function called add_three_numbers(a, b, c)
# # It should print the sum of the three numbers
# #
# # Expected output:
# # 12
# #
# # Function call:
# # add_three_numbers(3, 4, 5)

# # def add_three_numbers(a, b, c):
# #     print(a + b + c)

# # add_three_numbers(3, 4, 5)



# # -------------------------
# # EXERCISE 9
# # -------------------------
# # Create a function called repeat_word(word)
# # It should print the word 3 times on the same line
# #
# # Expected output:
# # hi hi hi
# #
# # Function call:
# # repeat_word("hi")

# # def repeat_word(word):
# #     print(word * 3)

# # repeat_word("hi ")


# # -------------------------
# # EXERCISE 10
# # -------------------------
# # Create a function called ask_name_and_greet()
# # The function should:
# # - Ask the user to enter their name
# # - Print: Hello <name>
# #
# # Expected input:
# # Winnie
# #
# # Expected output:
# # Hello Winnie
# #
# # Function call:
# # ask_name_and_greet()

# # def ask_name_and_greet():
# #     name = input("Enter your name: ")
# #     print(f"Hello {name.strip().capitalize()}")

# # ask_name_and_greet()








# # def get_total_length(*strs):
# #     len_str = [len(str1) for str1 in strs]
# #     return(sum(len_str))

# # print(get_total_length("hi", "hello"))



# # def highest_score(**name_and_scores):
# #     high_score = max(highest_score.values())
# #     return high_score


# # print(highest_score(Ada=72, Bisi=89, Charles=67))





# # def multiply(list_items):
# #     result = 1
# #     for item in list_items:
# #         result *= item
# #     return result

# # print(multiply([1, 2, 3, -4]))


# # def multiply_first_two(*nums):
# #     return nums[0] * nums[1]

# # print(multiply_first_two(3, 5, 9, 2))
# # print(multiply_first_two(10, 2, 7))



# # -----------------------------------------------WEDNESDAY ASSIGNMENT--------------------------------------------------

# # 4 - 15



# # 4. Create a function called describe_books that prints out each book title and its author.

# # def describe_books(**book_title_and_author):
#     # for book_title, author in book_title_and_author.items():
#         # print(f"{book_title} is written by {author}")
  

# # Test Data:
# # describe_books(Hamlet="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert")
# # describe_books(**{"Matilda": "Roald Dahl", "1984": "George Orwell"})

# # Expected Output:
# # Hamlet is written by Shakespeare
# # ThingsFallApart is written by Chinua Achebe
# # Dune is written by Frank Herbert
# # Matilda is written by Roald Dahl
# # 1984 is written by George Orwell




# # 5. Create a function called total_age that returns the sum of all the ages given.


# # def total_age(*ages):
#     # return sum(ages)

# # Test Data:
# # print(total_age(12, 30, 18))
# # print(total_age(40, 25))

# # Expected Output:
# # 60
# # 65


# # 6. Create a function called list_countries that prints out each country passed in.


# # def list_countries(*countries):
#     # for country in countries:
#         # print(country)

# # Test Data:
# # list_countries("Nigeria", "Ghana", "Kenya")
# # list_countries("Canada", "Mexico")

# # Expected Output:
# # Nigeria
# # Ghana
# # Kenya
# # Canada
# # Mexico

# # 7. Create a function called student_details that prints each student’s name and score.


# # def student_details(**name_and_score):
#     # for name, score in name_and_score.items():
#         # print(f"{name} scored {score}")

# # Test Data:
# # student_details(Fola=78, Muna=88, Kola=65)
# # student_details(Sandra=91, Alex=85)

# # Expected Output:
# # Fola scored 78
# # Muna scored 88
# # Kola scored 65
# # Sandra scored 91
# # Alex scored 85


# # 8. Create a function called average_score that returns the average of all scores passed in.


# # def average_score(*nums):
#     # return sum(nums) / len(nums) 

# # Test Data:
# # print(average_score(50, 60, 70))
# # print(average_score(80, 90))

# # Expected Output:
# # 60.0
# # 85.0

# # 9. Create a function called total_price that adds up the prices of all items passed as keyword arguments.


# # def total_price(**item_and_price):
#     # return sum(item_and_price.values())

# # Test Data:
# # print(total_price(bread=500, milk=1200, eggs=700))
# # print(total_price(book=1500, pen=200))

# # Expected Output:
# # 2400
# # 1700


# # 10. Create a function called first_and_last that prints the first and last values passed in.


# # def first_and_last(*items):
#     # print(f"First: {items[0]}, Last: {items[-1]}")

# # Test Data:
# # first_and_last(4, 10, 6, 9, 12)
# # first_and_last("a", "b", "c", "d")

# # Expected Output:
# # First: 4, Last: 12
# # First: a, Last: d


# # 11. Create a function called describe_animals that prints out animal and their sound.


# # def describe_animals(**animal_and_sound):
#     # for animal, sound in animal_and_sound.items():
#         # print(f"{animal} makes the sound {sound}")

# # Test Data:
# # describe_animals(cat="meow", dog="bark", cow="moo")
# # describe_animals(lion="roar", snake="hiss")

# # Expected Output:
# # cat makes the sound meow
# # dog makes the sound bark
# # cow makes the sound moo
# # lion makes the sound roar
# # snake makes the sound hiss


# # 12. Create a function called total_characters that returns how many characters in total exist in all keyword values.


# # def total_characters(**letter_and_value):
# #     # return sum(len(letter_and_value.values()))
# #     length_of_values = []
# #     for value in letter_and_value.values():
# #         length_of_values.append(len(value))
# #     return sum(length_of_values)

# # # Test Data:
# # print(total_characters(a="banana", b="mango", c="kiwi"))
# # print(total_characters(x="hi", y="there"))

# # Expected Output:
# # 15
# # 7


# # 13. Create a function called find_minimum that returns the smallest number from all the values passed in.


# # def find_minimum(*nums):
#     # return min(nums)

# # Test Data:
# # print(find_minimum(99, 45, 12, 88))
# # print(find_minimum(8, 3, 7))

# # Expected Output:
# # 12
# # 3


# # 14. Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.


# # def sum_scores_and_bonuses(*nums, **scores_and_bonuses):
# #     sum_all = 0
# #     sum_all += sum(nums)
# #     for bonus in scores_and_bonuses.values():
# #         sum_all += bonus
# #     return sum_all

# # # Test Data:
# # print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# # print(sum_scores_and_bonuses(100, bonus=50))

# # Expected Output:
# # 50
# # 150


# # 15. Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).


# # def longest_word(*words, **keywords):
# #     for keyword in keywords.values():
# #         for word in words:
# #             longest_word = word
# #             if len(word) > len(longest_word):
# #                 longest_word = word
# #             if len(keyword) > len(longest_word):
# #                 longest_word = keyword
# #             if len(keyword) > len(longest_word):
# #                 longest_word = len(keyword)

# #     return(longest_word)

# # # Test Data:
# # print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# # print(longest_word("short", name="exaggeration", tool="pen"))

# # Expected Output:
# # hippopotamus
# # exaggeration
# # ====================================ASSIGNMENT===========================================



# # 1 - 17



# # 1. Write a function sum_numbers(a, b) that returns the sum of two numbers.

# # def sum_numbers(a, b):
#     # return a + b

# # 2. Write a function is_even(n) that returns True if n is even and False if n is odd.

# # def is_even(n):
#     # return n % 2 == 0

# # 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

# # def is_prime(n):
#     # if n <= 1:
#         # return False
#     # for i in range(2, int(n ** 0.5) + 1):
#         # if number % i == 0:
#             # return False

#     # return True

# # 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and 
# # returns all the prime numbers up to n.
# # 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both 
# # numbers are even, but returns the greater if one or both numbers are odd.

# # def lesser_of_two_evens(a, b):
# #     if a % 2 == 0 and b % 2 == 0:
# #         return min(a, b)

# #     return max(a, b)

# # 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if 
# # both words begin with the same letter.
# # is_alliteration(‘Levelheaded llama’) —> True
# # is_alliteration(‘Crazy Kangaroo’) –> False

# # def is_alliteration(two_word_string):
# #     seperated_words = two_word_string.split()

# #     if len(seperated_words) != 2:
# #         return False

# #     return seperated_words[0][0].lower() == seperated_words[1][0].lower()


# # 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# # old_macdonald(‘macdonald’) —> MacDonald
# # Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# # def old_macdonald(macdonald):
#     # macdonald[3] = macdonald[3].upper()
#     # return macdonald.capitalize()
# # print(old_macdonald("macdonald")) 

# # 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it 
# # contains 007 in order.
# # spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# # spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# # spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
# # 9. Write a function vol(radius) that computes the volume of a sphere given its radius.
# # 10. Write a function range_check(num, low, high) that checks whether a number is in a given 
# # range (inclusive of high and low).
# # 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase 
# # letters and lowercase letters.

# # def upper_lower(text):
# #     num_of_upper = 0
# #     num_of_lower = 0
# #     for char in text:
# #         if char == char.upper():
# #             num_of_upper += 1
# #         if char == char.lower():
# #             num_of_lower += 1
# #         return f"Number of uppercase: {num_of_upper}, Number of lowercase: {num_of_lower}"

# # 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique 
# # elements of the first list. Do not use the set() constructor.
# # 13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# # 	Sample List: [1, 2, 3, -4]
# # 	Expected output: -24

# # def multiply(list_items):
#     # result = 1
#     # for item in list_items():
#         # result *= item
#     # return result

# #  14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# # 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# # 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# # 	Hint: Import and use the string module.
# #  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# # 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# # 	spar, formed from rasp.
# #  16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# # 	(BMI) given weight in kilograms and height in meters.
# #  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# # 	simple interest given principal amount, interest rate, and time (in years).
# # def calculate_simple_interest(principal, rate, time):
#     # return (principal * rate * time) / 100

# # print(calculate_simple_interest(200, 5, 1))










# # ----------------------------------------------OOP----------------------------------------------------



# # class Person:
# #     def __init__(self, first_name: str, last_name: str, age: int, height: float, is_male: bool):
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.age = age
# #         self.height = height
# #         self.is_male = is_male

# #     def walk(self):
# #         print("I am walking")
# #     def run(self):
# #         print("I am running")
# #     def intro(self):
# #         print(f"My name is {self.first_name} {self.last_name}")

# # person1 = Person("Adil", "Hassan", 16, 1.67, True)
# # print(person1.age)
# # person1.intro()
# # person1.run()


# # person2 = Person("Francis", "Ezebue", 18, 1.79, True)
# # print(person2.age)
# # person2.intro()
# # person2.run()




# # class Car:
# #     def __init__(self, brand: str, model: str, year: int, horsepower: int, fuel_type: str):
# #         self.brand = brand
# #         self.model = model
# #         self.year = year
# #         self.horsepower = horsepower 
# #         self.fuel_type = fuel_type
        
# #     def car_info(self):
# #         return f"This is a {self.year} {self.brand} {self.model} with {self.horsepower} HP runing on {self.fuel_type}"

# # toyota = Car("Toyota", "Camry TRD", 2021, 301, "Petrol")
# # print(toyota.car_info())

# # bmw = Car("BMW", "M340i", 2020, 382, "Petrol")
# # print(bmw.car_info())

# # ford = Car("Ford", "F-150 PowerBoost Hybrid", 2022, 430, "Hybrid")
# # print(ford.car_info())




# # class Student:
# #     def __init__(self, name: str, age: int, grades: list[int]):
# #         self.name = name
# #         self.age = age
# #         self.grades = grades

# #     def average_grade(self):
# #         return sum(self.grades) / len(self.grades)

# #     def is_passing(self):
# #         return self.average_grade() >= 50

# # student1 = Student("Adil", 16, [50, 90, 80, 30, 40])
# # print(student1.average_grade())
# # print(student1.is_passing())

# # student2 = Student("Blah blah blah", 17, [2, 50, 20, 30, 40])
# # print(student2.average_grade())
# # print(student2.is_passing())




# # ----------------------------------------------OOP----------------------------------------------------





# #OOP ASSIGNMENT



# # 1. Fill in the Line class methods to accept coordinates as a pair of tuples and 
# # return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


# # class Line:
# #     def __init__(self, coor1: tuple, coor2: tuple): 
# #         # self.coor1 = coor1
# #         # self.coor2 = coor2
# #         self.x1 = coor1[0]
# #         self.y1 = coor1[1]
# #         self.x2 = coor2[0]
# #         self.y2 = coor2[1]

# #     def distance(self):
# #         # x1 = self.coor1[0]
# #         # y1 = self.coor1[1]
# #         # x2 = self.coor2[0]
# #         # y2 = self.coor2[1]
# #         return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) ** 0.5

# #     def slope(self):
# #         # x1 = self.coor1[0]
# #         # y1 = self.coor1[1]
# #         # x2 = self.coor2[0]
# #         # y2 = self.coor2[1]
# #         return (self.y2 - self.y1) / (self.x2 - self.x1)

# # # EXAMPLE EXECUTION

# # coordinatel = (3,2)
# # coordinate2 = (8,10)

# # line_1 = Line(coordinatel, coordinate2)

# # print(line_1.distance())  # 9.433981132056603
# # print(line_1.slope())  # 1.6




# # 2.	Fill in the class
# # import math
# # pi = math.pi

# # class Cylinder:
# #     def __init__(self, height=1, radius=1):
# #         self.height = height
# #         self.radius = radius

# #     def volume (self):
# #         return round(pi * (self.radius ** 2) * self.height, 2)

# #     def surface_area(self):
# #         return round((2 * pi * self.radius) * (self.height + self.radius), 1) 

# # # EXAMPLE EXECUTION

# # cylinder = Cylinder(2,3)
# # print(cylinder.volume())  # 56.52
# # print(cylinder.surface_area())  # 94.2


# # 1. Create a class called Laptop with the following attributes:
# #    - brand
# #    - ram (in GB)
# #    - storage (in GB)
# #    - price
# #
# #    The class should have two methods:
# #    - upgrade_ram(extra_ram): increases the ram by extra_ram
# #    - laptop_info(): returns "{brand} laptop with {ram}GB RAM and {storage}GB storage costs {price}."
# #
# #    After defining the class, create 2 different Laptop objects with different values.


# class Laptop:
#     def __init__(self, brand: str, ram: int, storage: int, price: float):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.price = price
#     def upgrade_ram(self, extra_ram):
#         self.ram += extra_ram
#         return self.ram
#     def laptop_info(self):
#         return f"{self.brand} laptop with {self.ram}GB RAM and {self.storage}GB storage costs {self.price}."

# laptop1 = Laptop("HP Elitebook", 16, 512, 550_000)
# laptop1 = Laptop("HP Elitebook", 8, 256, 680_000)

# # 2. Create a class called Employee with the following attributes:
# #    - name
# #    - position
# #    - salary
# #
# #    The class should have two methods:
# #    - give_raise(amount): increases salary by amount
# #    - employee_info(): returns "{name} works as a {position} and earns {salary} per year."
# #
# #    After defining the class, create 3 different Employee objects with different values.

# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position 
#         self.salary = salary
#     def give_raise(self, amount):
#         self.salary += amount
#         return self.salary
#     def employee_info(self):
#         return f"{self.name} works as a {self.position} and earns {self.salary} per year."

# # employee1 = Employee("James", "HR", 400_000)
# # employee2 = Employee("Jack", "Secretary", 300_000)
# # employee3 = Employee("Juliet", "Manager", 600_000)



# # 3. Create a class called Phone with the following attributes:
# #    - brand
# #    - model
# #    - battery_percentage
# #
# #    The class should have two methods:
# #    - charge(amount): increases battery_percentage by amount (do not exceed 100)
# #    - phone_status(): returns "{brand} {model} battery is at {battery_percentage}%."
# #
# #    After defining the class, create 2 different Phone objects with different values.


# class Phone:
#     def __init__(self, brand, model, battery_percentage):
#         self.brand = brand
#         self.model = model
#         self.battery = battery_percentage
#     def charge(self, amount):
#         self.battery = min(self.battery + amount, 100)
#         return self.battery
#     def phone_status(self):
#         return f"{self.brand} {self.model} battery is at {self.battery}%."

# phone1 = Phone("Apple", "Iphone 17 air", 60)
# print(phone1.charge(50))
# print(phone1.phone_status())
# # phone2 = Phone("Google", "Pixel 8", 19)
# # print(phone2.charge(40))
# # print(phone2.phone_status())



# # 4. Create a class called Product with the following attributes:
# #    - name
# #    - price
# #    - quantity_in_stock
# #
# #    The class should have three methods:
# #    - restock(amount): increases quantity_in_stock by amount
# #    - sell(amount): decreases quantity_in_stock by amount
# #    - inventory_value(): returns total value of stock (price * quantity_in_stock)
# #
# #    After defining the class, create 3 different Product objects with different values.

# class Product:
#     def __init__(self, name, price, quantity_in_stock):
#         self.name = name
#         self.price = price
#         self.quantity = quantity_in_stock

#     def restock(self, amount):
#         self.quantity += amount
#         return self.quantity
#     def sell(self, amount):
#         self.quantity -= amount
#     def inventory_value(self):
#         self.price *= self.quantity

# product1 = Product("milk", 300, 500)
# # print(product1.restock(2000))
# # product2 = Product("sugar", 800, 300)
# # product3 = Product("yam", 10_000, 800)



# # 5. Create a class called Course with the following attributes:
# #    - course_name
# #    - instructor
# #    - students (a list of student names)
# #
# #    The class should have two methods:
# #    - add_student(name): adds a student to the students list
# #    - total_students(): returns the number of students enrolled
# #
# #    After defining the class, create 2 different Course objects with different values.

# class Course:
#     def __init__(self, course_name: str, instructor: str, students: list[str]):
#         self.course_name = course_name
#         self.instructor = instructor
#         self.students = students
#     def add_student(self, name):
#         self.students.append(name)
#         return self.students
#     def total_students(self):
#         return len(self.students)

# course1 = Course("EEE", "Mr Agbaje", ["Adil", "Francis", "Pelumi", "Ahmad"])
# course2 = Course("BME", "Mr Komo", ["Lida", "Caesar", "Alli", "Ibk"])

# print(course1.add_student("Mibo"))
# print(course1.total_students())


# 6. Create a class called Circle with the following attributes:
#     - radius
#
#     The class should have two methods:
#     - area(): returns 3.14 * radius * radius
#     - circumference(): returns 2 * 3.14 * radius
#
#     After defining the class, create 3 different Circle objects with different values.


# class Circle:
#     def __init__(self, radius: int):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def circumference(self):
#         return 2 * 3.14 * self.radius

# circle1 = Circle(7)
# circle2 = Circle(14)
# circle3 = Circle(15)