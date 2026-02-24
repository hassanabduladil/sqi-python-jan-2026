# # # # first assignment 1 - 20

# # # first_name = "John"
# # # last_name = "Smith"
# # # print(first_name + " " + last_name)

# # # word = "Python"
# # # print(word[:1])

# # # greeting = "Hello"
# # # print(f"{greeting} Alice.")

# # # part1 = "Data"
# # # part2 = "Science"
# # # print(part1 + part2)

# # # phrase = "Welcome"
# # # print(phrase[-1])

# # # food = "pizza"
# # # print(f"I love {food}.")

# # # str_1 = "Good"
# # # str_2 = "Morning"
# # # print(str_1 + " " + str_2)

# # # text = "Concatenate"
# # # print(text[5])

# # # age = 25
# # # print(f"I am {age} years old.")

# # # city = "New"
# # # space = " "
# # # country = "York"
# # # print(city + space + country)

# # # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # # print(alphabet[9])

# # # day = "Sunday"
# # # activity = "hiking"
# # # print(f"On {day}, I am going {activity}")

# # # a = "Super"
# # # b = "Hero"
# # # print(a + b)

# # # universe = "MilkyWay"
# # # print(universe[-3])

# # # item = "book"
# # # price = 12.99
# # # print(f"The price of the {item} is {price}")

# # # hello = "Hello"
# # # world = "World"
# # # print(hello + ", " + world)

# # # sequence = "ABCDEFG"
# # # print(sequence[4])

# # # language = "Python"
# # # print(f"I am learning {language}")

# # # start = "Once upon a"
# # # end = " time"
# # # print(start + end)

# # # sports = "Basketball"
# # # print(sports[1])

# # # # second assignment 7, 9, 10, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44

# # # # 7
# # # message = "Hello, "
# # # print(f"{message}Alice")

# # # # 9
# # # language = "Python"
# # # print(language[0:7:5])

# # # # 10
# # # # language[2] = a
# # # # TypeError: 'str' object does not support item assignment

# # #35 - 44
# # # course_name = "Introduction to Python"
# # # print(course_name[:12])
# # # print(course_name[-6:])

# # # quote = "To be or not to be, that is the question"
# # # print(quote[:18])
# # # print(quote[20:])

# # # phrase = "A journey of a thousand miles begins with a single step"
# # # print(phrase[-5:])
# # # print(phrase[:-7])

# # # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # # print(alphabet[::2])
# # # print(alphabet[::3])

# # # word = "tenet"
# # # print(word[::-1])

# # # sentence = "Learning Python is fun and rewarding!"
# # # print(sentence[9:20])
# # # print(sentence[:11:2])
# # # print(sentence[::3])

# # # programming_language = "JavaScript"
# # # print(programming_language[:1])
# # # print(programming_language[-1:])

# # # data = "DataScience"
# # # print(data[4:])

# # # greeting = "Good Morning!"
# # # print(greeting[::2])

# # # name = "Alexander"
# # # print(name[:3] + name[-3:])

# # # 1. Create a string variable username with the value "coder123".
# # #    Print the last two characters of the string.
# # #    Expected output:
# # #    23
# # username = "coder123"
# # print(username[-2:])

# # # 2. Given the string email = "admin@example.com",
# # #    print everything before the "@" symbol using indexing or slicing.
# # #    Expected output:
# # #    admin
# # email = "admin@example.com"
# # print(email[:5])

# # # 3. Create variables product = "Laptop" and quantity = 3.
# # #    Use string interpolation to print:
# # #    "You ordered 3 Laptop(s)"
# # #    Expected output:
# # #    You ordered 3 Laptop(s)
# # product = "Laptop"
# # quantity = 3
# # print(f"You ordered {quantity} {product}(s)")

# # # 4. Given the string password = "securePass",
# # #    print the 3rd character from the end using negative indexing.
# # #    Expected output:
# # #    r
# # password = "securePass"
# # print(password[-6])

# # # 5. Create string variables prefix = "api", version = "v1", and separator = "/".
# # #    Concatenate them to form "api/v1" and print it.
# # #    Expected output:
# # #    api/v1
# # prefix = "api"
# # version = "v1"
# # seperator = "/"
# # equation = prefix + seperator + version
# # print(equation)

# # # 6. Given the string filename = "report.pdf",
# # #    print only the file extension (without the dot).
# # #    Expected output:
# # #    pdf
# # filename = "report.pdf"
# # print(filename[-3:])

# # # 7. Create variables first = "Open", middle = "AI", and last = "Labs".
# # #    Use string interpolation to print:
# # #    "Open AI Labs"
# # #    Expected output:
# # #    Open AI Labs
# # first = "Open"
# # middle = "AI"
# # last = "Labs"
# # print(f"{first} {middle} {last}")

# # # 8. Given the string slogan = "Build fast. Build right.",
# # #    print the character at index 11.
# # #    Expected output:
# # #    .
# # slogan = "Build fast. Build right."
# # print(slogan[10])

# # # 9. Create a variable score = 87.
# # #    Use string interpolation to print:
# # #    "Your final score is 87%"
# # #    Expected output:
# # #    Your final score is 87%
# # score = 87
# # print(f"Your final score is {score}%")

# # # 10. Given the string code = "PYTHONIC",
# # #     print the first character and the last character joined together as a single string.
# # #     Expected output:
# # #     PC
# # code = "PYTHONIC"
# # print(code[0] + code[-1])


# # 2nd monday assignent

# # 1. Given the string file_path = "/usr/local/bin/python",
# #    use slicing to print:
# #    a) The string "python"
# #    b) The string "/usr/local"
# #    Expected output:
# #    python
# #    /usr/local
# file_path = "/usr/local/bin/python"
# print(file_path[-6:])
# print(file_path[:10])

# # 2. Given the string headline = "Breaking News: Market Crash Today",
# #    use slicing to print:
# #    a) "Breaking News"
# #    b) "Market Crash Today"
# #    Expected output:
# #    Breaking News
# #    Market Crash Today
# headline = "Breaking News: Market Crash Today"
# print(headline[:13])
# print(headline[15:])

# # 3. Given the string message = "System reboot required immediately",
# #    use slicing to print the last 10 characters.
# #    Expected output:
# #    immediately
# message = "System reboot required immediately"
# print(message[-11:])

# # 4. Given the string letters = "abcdefghijklmnopqrstuvwxyz",
# #    use slicing to print:
# #    a) Every second letter starting from index 0
# #    b) Every third letter starting from index 1
# #    Expected output:
# #    acegikmoqsuwy
# #    behknqtwz
# letters = "abcdefghijklmnopqrstuvwxyz"
# print(letters[::2])
# print(letters[1::3])

# # 5. Given the string palindrome = "racecar",
# #    use slicing to reverse the string and print the result.
# #    Expected output:
# #    racecar
# palindrome = "racecar"
# print(palindrome[::-1])

# # 6. Given the string description = "Slicing strings makes Python powerful",
# #    use slicing to print:
# #    a) Characters from index 8 to 15
# #    b) Every second character from index 0 to 12
# #    Expected output:
# #    strings
# #    Slcnsrn
# description = "Slicing strings makes Python powerful"
# print(description[8:16])
# print(description[:13:2])

# # 7. Given the string framework = "DjangoRestFramework",
# #    use slicing to print:
# #    a) The first 6 characters
# #    b) The last 9 characters
# #    Expected output:
# #    Django
# #    Framework
# framework = "DjangoRestFramework"
# print(framework[:6])
# print(framework[-9:])

# # 8. Given the string dataset = "UserActivityLogs",
# #    use slicing to print the substring "Activity".
# #    Expected output:
# #    Activity
# dataset = "UserActivityLogs"
# print(dataset[4:12])

# # 9. Given the string warning = "Unauthorized access detected!",
# #    use slicing to print every second character.
# #    Expected output:
# #    Uatuizdace eetd
# warning = "Unauthorized access detected!"
# print(warning[::2])

# # 10. Given the string full_name = "Christopher",
# #     use slicing to print the first 4 characters
# #     concatenated with the last 4 characters.
# #     Expected output:
# #     Chrispher
# full_name = "Christopher"
# slice_first_4 = full_name[:4]
# print(slice_first_4 + full_name[-4:])