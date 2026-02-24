# TUPLES



record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, pos), (dept1, dept2) = record
_, (age, _), (dept1, _) = record

print(age)
print(dept1)


# order = (
#     "ORD-2049",
#     {
#         "customer": ("Alice", 24),
#         "delivery": ("Lagos", ("Ikeja", 1000))
#     },
#     ["Laptop", "Mouse", "Keyboard"]
# )


# Using tuple unpacking and nested destructuring only, extract:
# The customer’s age
# The delivery city (e.g. "Ikeja")
# The first item in the order

# Ignore all other values.

# Expected Output:
# 24
# Ikeja
# Laptop


# record = (
#     "STD-8821",
#     ("John", (19, "Computer Science")),
#     [("Math", 78), ("Physics", 85), ("Chemistry", 69)]
# )

# _, (name, (_, _)), ((_, _,) (_, score), (_, _))  = record
# print(name)
# print(score)

trip = (
    "TRP-450",
    ("Peace Bus", ("Abuja", "Kaduna")),
    (
        ("Driver", ("Samuel", 45)),
        ("Conductor", ("Amina", 32))
    ),
    [12000, 13500, 15000]
)
_, (_, (_, destination)), ((_), (job2, (_))), [_, _, _] = trip
print(destination)
print(job2)