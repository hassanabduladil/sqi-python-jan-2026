
def is_password_strong(password: str):

    is_at_least_8_chars_long = len(password) >= 8

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    special_chars = "!@#$%^&*()"

    has_special_char = any(char in special_chars for char in password)

    return password, is_at_least_8_chars_long and has_upper and has_lower and has_digit and has_special_char

password1 = "p@ssw0rd123"
password2 = "Pass123!"
password3 = "12345678"
password4 = "P@ssw0rd!123"
password5 = "123456789"

for password in [password1, password2, password3, password4, password5]:
    password_checked, password_is_strong = is_password_strong(password)
    suffix = "" if password_is_strong else "not"
    print(f"{password_checked} is {suffix} strong")



def is_password_strong(password: str):

    is_at_least_8_chars_long = len(password) >= 8

    has_upper = False
    has_lower = False
    has_digit = False
    has_special_char = False

    special_chars = "!@#$%^&*()"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    return password, is_at_least_8_chars_long and has_upper and has_lower and has_digit and has_special_char
    

password1 = "p@ssw0rd123"
password2 = "Pass123!"
password3 = "12345678"
password4 = "P@ssw0rd!123"
password5 = "123456789"

for password in [password1, password2, password3, password4, password5]:
    password_checked, password_is_strong = is_password_strong(password)
    suffix = "" if password_is_strong else "not"
    print(f"{password_checked} is {suffix} strong")