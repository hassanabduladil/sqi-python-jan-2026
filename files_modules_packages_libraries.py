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


# with open("names.txt", "r") as f:
#     contents = f.read()


# with open("uppercase_names.txt", "w") as f:
#     f.write(contents.upper())



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

# with open("words.txt", "r") as f:
#     lines = f.readlines()

# reversed_lines = [line.strip()[::-1] + "\n" for line in lines]
# reversed_lines = "".join(reversed_lines)
# print(reversed_lines)

# with open("reversed_words.txt", "w") as f:
#     f.write(reversed_lines)

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
# ============================================================




# with - context manager


# try:
#     with open("does_not_exist.txt", "r") as f:
#         contents = f.read()
# except FileNotFoundError as e:
#     print("File not found")
#     contents = ""

# print(contents)

# contents = None

# try:
#     with open("does_not_exist.txt", "r") as f:
#         contents = f.read()
# except FileNotFoundError as e:
#     pass
# finally:
#     if contents is not None:
#         f.close()

# script



# datetime

# from datetime import datetime

# today = datetime.now()



# import datetime

# today = datetime.datetime.now()

# print(today)

# print(today + ".")

# strftime - str format time - datetime to str 
# strptime - str parse time - str to datetime

# print(today.strftime("%d/%m/%Y %H:%M:%S"))
# print(today.strftime("%Y-%m-%d %H:%M:%S"))

# current_year = today.year

# date = "2025-02-17"

# print(datetime.datetime.strptime(date, "%Y-%m-%d").date())


# birth_date = input("Enter your birth date in this format (e.g. February 4): ")

# birth_date = datetime.datetime.strptime(f"{birth_date} {current_year}", "%B %d %Y").date()

# today_date = today.date()

# if today_date < birth_date:
#     print("it is not yet your birthday")
# elif today_date == birth_date:
#     print("Happy birthday to you! 🎉")
# else:
#     print("Your birthday has passed this year")


# import datetime
# import sys
# import time

# today = datetime.datetime.now()

# print(today)

# three_days_from_today = today + datetime.timedelta(3)
# print("three_days_from_today:", three_days_from_today)
# two_weeks_ago = today - datetime.timedelta(weeks=2)
# print("two_weeks_ago:", two_weeks_ago)


# # twenty_four_hours_from_now = today + datetime.timedelta(1)
# twenty_four_hours_from_now = today + datetime.timedelta(seconds=10)

# print(twenty_four_hours_from_now)

# while today < twenty_four_hours_from_now:
#     diff = twenty_four_hours_from_now - today
#     hours, remaining_seconds = divmod(diff.total_seconds(), 3600)
#     minutes, seconds = divmod(remaining_seconds, 60)

#     # Convert to integers if needed
#     hours = int(hours)
#     minutes = int(minutes)
#     seconds = int(seconds)

#     sys.stdout.write(f"\r{hours}:{minutes}:{seconds}") 
#     sys.stdout.flush()
#     time.sleep(0.2)

#     today = datetime.datetime.now()
# else:
#     print("\nCountdown completed!")



import math

print(math.sqrt(16))
sixty_degress_to_radians = math.radians(60)
print(math.cos(sixty_degress_to_radians))


print(math.log(100, 10))

print(math.log10(100))

