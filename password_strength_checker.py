# password = "passWord123!"

# is_at_least_8_chars_long = len(password) >= 8

# has_upper = any(char.isupper() for char in password)
# has_lower = any(char.islower() for char in password)
# digits = "0123456789"
# has_digits = any(char in digits for char in password)
# import string
# letters = string.ascii_letters
# has_special_characters = any(char not in digits and char not in letters for char in password)


# print(all([is_at_least_8_chars_long, has_upper, has_lower, has_digits, has_special_characters]))
# print(is_at_least_8_chars_long and has_upper and has_lower and has_digits and has_special_characters)



password = "passWord123!"
digits = "0123456789"
import string
letters = string.ascii_lowercase
conditions = []

for char in password:
    if len(password) >= 8:
        conditions.append(True)
    if char in digits:
        conditions.append(False)
    if char.islower():
        conditions.append(False)
    if char.isupper():
        conditions.append(False)
    if char in digits or char in letters:
        conditions.append(False)

print((conditions))