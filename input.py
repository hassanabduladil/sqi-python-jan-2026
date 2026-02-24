# # # # # # print("Hello " + input("What is your name? ") + "!")

# # # # # username = input("What is your name? ")
# # # # # length = len(username)
# # # # # print(length)

# # # # # print(len(input("What did you eat? ")))

# # # # print("Welcome to the Band Name Generator.")
# # # # # input("What is the name of the city you grew up in? ")
# # # # city = input("What is the name of the city you grew up in?\n")
# # # # # print(city)
# # # # pet = input("What is your pet's name?\n")
# # # # # print(pet)
# # # # print("Your band name could be " + city + " " + pet)

# # # # print("Adil"[0])
# # # name = "Adil"
# # # print(name[0])

# # len("Hello")

# print(type("Hello"))
# print(type(123))
# print(type(123.45))
# print(type(True))

# print(3 * 3 + 3 / 3 -3)
# print(3 + 3 * 3 / 3 -3)

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
# percent = input("How much tip would you like to give? 10, 12 or 15? ")
percent = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
easy_method_percentage = percent / 100 + 1
final_amount = round(total_bill * easy_method_percentage / people, 2)
print(f"Each person should pay ${final_amount}")