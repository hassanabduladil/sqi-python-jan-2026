# ---------------------------------------------OOP---------------------------------------------------------




# ---------------------------------------------CLASS ATTRS AND INHERITANCE------------------------------------------------


# class CartItem:
#     def __init__(self, name: str, price: int, no_of_items: int):
#         self.name = name
#         self.price = price
#         self.no_of_items = no_of_items
    
#     def total(self):
#         return self.price * self.no_of_items


# class Cart:
#     def __init__(self, cartitems: list[CartItem]):
#         self.cartitems = cartitems

#     def cart_total(self):
#         return sum(cartitem.total() for cartitem in self.cartitems)


# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.cart_total())



# ============================================================
# EXERCISE: Vehicle Classes
# ============================================================
#
# 1. Create a class called Vehicle with the following:
#
#    _init_ receives: name (str), type (str), has_engine (bool),
#                       is_electric (bool), can_fly (bool), top_speed (int)
#
#    Store all parameters as instance attributes.
#    Also create an attribute called category:
#       - If top_speed is greater than 100, category should be "fast"
#       - Otherwise, category should be "slow"
#
#    Methods:
#       describe(self) -> str
#           Returns: "This is {name}. It is a {type}. Its top speed is {top_speed} km/h."
#
#       honk(self) -> str
#           Returns: "The {type} is honking"
#
#
# 2. Create a class called Bicycle that inherits from Vehicle.
#
#    _init_ receives: name, top_speed, gear_count
#
#    Calls the parent _init_ with the following fixed values:
#       type = "bicycle", has_engine = False, is_electric = False, can_fly = False
#       (name and top_speed come from the parameters)
#
#    After calling super()._init_, override category to be "eco-friendly"
#    Also store gear_count as an instance attribute.
#
#    Override describe(self):
#       Start by calling the parent's describe() method.
#       Append to it: " It has {gear_count} gears. It is {category}."
#       Return the full string.
#
#
# 3. Create the following objects and print their descriptions:
#
#    car = Vehicle("Thunderbolt", "Car", True, False, False, 200)
#    bicycle = Bicycle("Greenway", 25, 21)
#
#    print(car.describe())
#    print(bicycle.describe())
#
#
# EXPECTED OUTPUT:
#
# This is Thunderbolt. It is a Car. Its top speed is 200 km/h.
# This is Greenway. It is a bicycle. Its top speed is 25 km/h. It has 21 gears. It is eco-friendly.
#
# ============================================================



# class Vehicle:
#     def __init__(self, name: str, type: str, has_engine: bool, is_electric: bool, can_fly: bool, top_speed: int):
#         self.name = name
#         self.type = type
#         self.has_engine = has_engine
#         self.is_electric = is_electric
#         self.can_fly = can_fly
#         self.top_speed = top_speed
#         self.category = "fast" if self.top_speed > 100 else "slow"

#     def describe(self):
#           return f"This is {self.name}. It is a {self.type}. Its top speed is {self.top_speed} km/h."

#     def honk(self):
#           return f"The {self.type} is honking"

# class Bicycle(Vehicle):
#     def __init__(self, name, top_speed, gear_count):
#         super().__init__(name, "bicycle", False, False, False, top_speed)
#         self.gear_count = gear_count
#         eco_friendly = self.category
#         # new = Vehicle.describe() + f"It has {self.gear_count} gears. It is {self.category}."
#     def intro(self):
#         cycle_intro = super().describe()
#         cycle_intro += f"It has {self.gear_count} gears. It is {self.category}."
#         return cycle_intro


# car = Vehicle("Thunderbolt", "Car", True, False, False, 200)
# bicycle = Bicycle("Greenway", 25, 21)

# print(car.describe())
# print(bicycle.intro())





# ----------------------------ASSIGNMENT------------------------------------------------------


# 1.
# class OrderItem:
#     def __init__(self, product_name: str, quantity: int):
#         self.product_name = product_name
#         self.quantity = quantity


# class Order:
#     def __init__(self, items: list):
#         self.items = items


# class Warehouse:
#     def __init__(self, inventory: dict):
#         self.inventory = inventory

#     def place_order(self, order: Order):
#         for item in order.items:
#             if item.product_name not in self.inventory:
#                 return False
#             if self.inventory[item.product_name] < item.quantity:
#                 return False

#         for item in order.items:
#             self.inventory[item.product_name] -= item.quantity

#         return True


# warehouse = Warehouse({
#     "laptop": 10,
#     "phone": 25,
#     "headphones": 50
# })


# order1 = Order([
#     OrderItem("laptop", 2),
#     OrderItem("phone", 5)
# ])

# order2 = Order([
#     OrderItem("laptop", 9), 
#     OrderItem("headphones", 2)
# ])

# print(warehouse.place_order(order1))
# # -> True

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# print(warehouse.place_order(order2))
# # -> False

# print(warehouse.inventory)
# # # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# order3 = Order([
#     OrderItem("tv", 7)
# ])

# print(warehouse.place_order(order3))


# print(warehouse.inventory)








# 2. Create a class called Playlist with the following attributes:
#    - name
#    - songs (a list of strings)
#
#    The class should have three methods:
#    - add_song(song): adds a new song title to the playlist
#    - total_songs(): returns the total number of songs
#    - show_songs(): returns all song titles as a comma-separated string
#
#    After defining the class, create a Playlist and add a few songs.


# class Playlist:
#     def __init__(self, name: str, songs: list[str]):
#         self.name = name
#         self.songs = songs

#     def add_song(self, song: str):
#         self.songs.append(song)

#     def total_songs(self):
#         return len(self.songs)
    
#     def show_songs(self):
#         return ", ".join(self.songs)


# # Example usage:
# pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# pl.add_song("Lose Yourself")
# pl.add_song("Can't Hold Us")

# print(pl.name, "has", pl.total_songs(), "songs")
# print("Songs:", pl.show_songs())

# Expected Output:
# Workout Jams has 4 songs
# Songs: Eye of the Tiger, Stronger, Lose Yourself, Can't Hold Us


# 3. Create a class called ShoppingCart with the following attributes:
#    - owner
#    - items (a dictionary where keys are item names and values are prices)
#
#    The class should have three methods:
#    - add_item(item, price): adds the item with its price
#    - total_cost(): returns the sum of all prices
#    - most_expensive(): returns the item with the highest price
#
#    After defining the class, create a ShoppingCart and add multiple items.

# class ShoppingCart:
#     def __init__(self, owner: str, items: dict):
#         self.owner = owner
#         self.items = items

#     def add_item(self, item, price):
#         self.items[item] = price
#         return self.items

#     def total_cost(self):
#         return sum(self.items.values())

#     def most_expensive(self):
#         return max(self.items.values())

# cart = ShoppingCart("Alice", {})

# cart.add_item("Apple", 2)
# cart.add_item("Banana", 3)
# cart.add_item("Milk", 4)
# cart.add_item("Laptop", 1000)

# print("Items:", cart.items)
# print("Total cost:", cart.total_cost())
# print("Most expensive item price:", cart.most_expensive())





# ---------------------------------------------CLASS ATTRS AND INHERITANCE------------------------------------------------







# ------------------------------------------ERRORS AND EXCEPTION HANDLING--------------------------------------

# while True:
#     from datetime import date
#     try:
#         user_age = int(input("Enter your age: "))
#         birth_year = date.today().year - user_age
#         # print(f"You were born in {birth_year}")
#         if user_age < 0:
#             print("Enter a valid age")
#             continue
#     except ValueError:
#         print("Enter a valid age")
#         continue
#     else:
#         print(f"You were born in {birth_year}")
#         break




# ASSIGNMENT--------------------


# 1. Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.

class NegativeNumberError(Exception):
    def __init__(self, number, *args):
        super().__init__(*args)
        self.number = number
    
def check_positive_number(number):
        number = int(number)
        if number < 0:
            raise NegativeNumberError(number, "Number cannot be negative")
        return number

try:
    print(check_positive_number(9))
except NameError:
    print("Not a number")
except NegativeNumberError as e:
    print(f"Invalid number: {e}")
except ValueError as e:
        print(f"Not a number: {e}")


# 2. Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.

def safe_divide(a, b):
    return a / b

try:
    print(safe_divide(12, 2))
except NameError:
    print("Num 1 or Num 2 are not numbers, please enter a valid number")
except ZeroDivisionError as e:
    print(f"Cannot divide by 0: {e}")
except TypeError as e:
    print(f"Num 1 or Num 2 are not numbers, please enter a valid number: {e}")
except ValueError as e:
    print("Cannot covert numbers to float")




# ------------------------------------------ERRORS AND EXCEPTION HANDLING--------------------------------------

# -----------------------------FILES AND MODULES---------------------------------------

# ------------------------------------------------------------
# 1. Read All Lines and Count Them
# ------------------------------------------------------------
# There is a file called "students.txt" with the following content:
#
# Alice
# Bob
# Charlie
# David
#
# Task:
# - Read all lines from the file.
# - Print the total number of students.
#
# Sample Execution:
# > python program.py
#
# Expected Output:
# Total students: 4

def main():
    with open("students.txt", "r") as f:
        lines = f.readlines()
    names = [line.strip() for line in lines]
    print(f"Total students: {len(names)}")

if __name__ == "__main__":
    main()

# ------------------------------------------------------------
# 2. Convert All Names to Uppercase and Save
# ------------------------------------------------------------
# File: "names.txt"
#
# john
# mary
# peter
#
# Task:
# - Read all names.
# - Convert each name to uppercase.
# - Write them into a new file called "uppercase_names.txt".
#
# After running the program,
# the new file should contain:
#
# JOHN
# MARY
# PETER

with open("names.txt", "r") as infile:
    names = infile.readlines()

with open("uppercase_names.txt", "w") as outfile:
    for name in names:
        outfile.write(name.strip().upper() + "\n")

# ------------------------------------------------------------
# 3. Remove Empty Lines
# ------------------------------------------------------------
# File: "data.txt"
#
# Apple
#
# Banana
#
# Orange
#
# Task:
# - Read all lines.
# - Remove empty lines.
# - Write the cleaned result into "cleaned_data.txt".
#
# Expected file content:
#
# Apple
# Banana
# Orange

with open("data.txt", "r") as infile:
    lines = infile.readlines()

with open("cleaned_data.txt", "w") as outfile:
    for line in lines:
        if line.strip():
            outfile.write(line)



# ------------------------------------------------------------
# 4. Count Words in File
# ------------------------------------------------------------
# File: "story.txt"
#
# Python is fun
# Coding is powerful
#
# Task:
# - Read the file.
# - Count the total number of words.
# - Print the total.
#
# Sample Execution:
# > python program.py
#
# Expected Output:
# Total words: 6

# with open("story.txt", "r") as infile:
#     content = infile.read()
#     words = content.split()
#     total_words = len(words)
#     print("Total words:", total_words)

# ------------------------------------------------------------
# 5. Append a New Log Entry
# ------------------------------------------------------------
# File: "log.txt"
#
# System started
#
# Task:
# - Append a new line that says: "User logged in"
#
# Expected file content after running:
#
# System started
# User logged in

# with open("log.txt", "a") as outfile:
#     outfile.write("User logged in\n")

# ------------------------------------------------------------
# 6. Reverse Each Line
# ------------------------------------------------------------
# File: "words.txt"
#
# cat
# dog
# fish
#
# Task:
# - Read each line.
# - Reverse the letters.
# - Save results into "reversed_words.txt".
#
# Expected content:
#
# tac
# god
# hsif

# with open("words.txt", "r") as infile:
#     lines = infile.readlines()

# with open("reversed_words.txt", "w") as outfile:
#     for line in lines:
#         outfile.write(line.strip()[::-1] + "\n")



# ------------------------------------------------------------
# 7. Add Line Numbers
# ------------------------------------------------------------
# File: "tasks.txt"
#
# Wash dishes
# Do homework
# Clean room
#
# Task:
# - Read the file.
# - Add numbers at the beginning of each line.
# - Save into "numbered_tasks.txt".
#
# Expected content:
#
# 1. Wash dishes
# 2. Do homework
# 3. Clean room

# with open("tasks.txt", "r") as infile:
#     tasks = infile.readlines()

# with open("numbered_tasks.txt", "w") as outfile:
#     for i, task in enumerate(tasks):
#         outfile.write(f"{i+1}. {task}")

# ------------------------------------------------------------
# 8. Filter Numbers Greater Than 50
# ------------------------------------------------------------
# File: "numbers.txt"
#
# 12
# 75
# 30
# 88
#
# Task:
# - Read all numbers.
# - Keep only numbers greater than 50.
# - Write them into "big_numbers.txt".
#
# Expected content:
#
# 75
# 88

with open("numbers.txt", "r") as infile:
    numbers = infile.readlines()

with open("big_numbers.txt", "w") as outfile:
    for number in numbers:
        number = int(number.strip())
        if number > 50:
            outfile.write(str(number) + "\n")

# ------------------------------------------------------------
# 9. Replace a Word
# ------------------------------------------------------------
# File: "message.txt"
#
# I love cats
#
# Task:
# - Replace the word "cats" with "dogs".
# - Save result into "updated_message.txt".
#
# Expected content:
#
# I love dogs

with open("message.txt", "r") as infile:
    content = infile.read()
new_content = content.replace("cats", "dogs")

with open("updated_message.txt", "w") as outfile:
    outfile.write(new_content)


# ------------------------------------------------------------
# 10. Merge Two Files
# ------------------------------------------------------------
# File 1: "first.txt"
#
# A
# B
#
# File 2: "second.txt"
#
# C
# D
#
# Task:
# - Read both files.
# - Combine their contents.
# - Write into "merged.txt".
#
# Expected content:
#
# A
# B
# C
# D

with open("first.txt", "r") as file1:
    content1 = file1.readlines()

with open("second.txt", "r") as file2:
    content2 = file2.readlines()

with open("merged.txt", "w") as outfile:
    outfile.writelines(content1)
    outfile.writelines(content2)


# ============================================================




# -----------------------------FILES AND MODULES---------------------------------------

import string

