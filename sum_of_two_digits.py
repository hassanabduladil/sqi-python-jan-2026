number = int(input("Write a two-digit number: "))
first_number = number // 10
last_number = number % 10
addition = first_number + last_number
print(f"The sum of {first_number} and {last_number} is {addition}")


number = (input("Write a two-digit number: "))
first_number = int(number[0])
last_number = int(number[1])
addition = first_number + last_number
print(f"The sum of {first_number} and {last_number} is {addition}")