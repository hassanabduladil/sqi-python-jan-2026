#                           Ordered             Indexed             Mutable         Allow Duplicates
# Lists                      Yes                  Yes                 Yes               Yes
# Tuples                     Yes                  Yes                 No                Yes
# Dictionaries           Yes, form Py 3.7+    Yes, but with keys      Yes       Dupliacte values, not duplicate keys
# Sets                        No                   No                 Yes               No




# my_dict = {"one": 1, "two": 2, "TWO": 2}

# my_dict["one"] = 1.0

# print(my_dict)


# my_set = {"one", "two", "three"}
# my_set = set(("one", "two", "three"))
# empty_dict = {}
# print(type(empty_dict))
# empty_set = set()
# my_set = set([1, 2, 3, 4])
# print(my_set)
# print(type(my_set))
# print(empty_set)
# print(type(empty_set))
# # print(type(my_set))
# # print(my_set)

# my_set = {"one", "two", "three"}
# print(my_set)


# print(set("hello"))

# my_set = {"one", "two", "three"}
# # print(my_set[0])
# print("one" in my_set)
# print("four" in my_set)


# my_set = {"one", "two", "three", "one"}

# print(my_set)

# my_set = {"one", True, "two", 1, "three", "one"}

# print(my_set)

# my_set = {"one", True, "two", 1, 0, False, "three", "one"}

# print(my_set)

# my_set = {"one", True, "two", 1, 0, False, "three", "one"}
# print(len(my_set))
# print(type(my_set))


# SET METHODS



# -----------------------------ADD TO A SET------------------------------

# animals = {"tortoise", "turtle", "tiger", "tigress"}
# animals.add("tasmanian devil")
# print(animals)

animals = {"tortoise", "turtle", "tiger", "tigress"}

# animals.update(["tasmanian devil", "t-rex"])
# animals.update({"tasmanian devil", "t-rex"})
# animals.update(("tasmanian devil", "t-rex"))
# animals.update({"tasmanian devil": "eufmkef", "t-rex": "wyfghu2ejifm"})

# print(animals)


# animals = {"tortoise", "turtle", "tiger", "tigress"}
# animals = animals.union({"tasmanian devil", "t-rex"})
# print(animals)


# animals = {"tortoise", "turtle", "tiger", "tigress"}
# other_animals = ["tasmanian devil", "t-rex"]
# all_animals = animals.union(other_animals)
# print(animals)
# print(other_animals)
# print(all_animals)


# animals = {"tortoise", "turtle", "tiger", "tigress"}
# other_animals = ["tasmanian devil", "t-rex"]
# all_animals = animals | other_animals
# print(animals)
# print(other_animals)
# print(all_animals)

# -----------------------------ADD TO A SET------------------------------


# -----------------------------INTERSECTION OF A SET------------------------------

# set_1 = {"red", "brown", "orange", "burgundy"}
# set_2 = {"blue", "green", "red", "purple", "brown", "yellow"}

# set_1.intersection_update(set_2)

# print(set_1)
# print(set_2)


# set_1 = {"red", "brown", "orange", "burgundy"}
# set_2 = ("blue", "green", "red", "purple", "brown", "yellow")

# intersection = set_1.intersection(set_2)

# print(set_1)
# print(set_2)
# print(intersection)


# set_1 = {"red", "brown", "orange", "burgundy"}
# set_2 = {"blue", "green", "red", "purple", "brown", "yellow"}

# intersection = set_1 & set_2
# # ampersand
# print(set_1)
# print(set_2)
# print(intersection)


# set_1 = {"red", "brown", "orange", "burgundy"}
# set_2 = {"blue", "green", "red", "purple", "brown", "yellow"}
# set_3 = {"violet", "indigo", "peach", "pink", "red"}

# intersection = set_1 & set_2 & set_3
# # intersection = set_1.intersection(set_2).intersection(set_3)
# # ampersand
# print(set_1)
# print(set_2)
# print(set_3)
# print(intersection)

# -----------------------------INTERSECTION OF A SET------------------------------


# -----------------------------DIFFERENCE OF SETS------------------------------

# set_1 = {"red", "brown", "orange", "burgundy"}
# set_2 = {"blue", "green", "red", "purple", "brown", "yellow"}


# # set_1.difference_update(set_2)

# set3 = set_1.difference(set_2)

# # print(set_1)
# print(set3)

# 7 - 4


# |||||||


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# # set3 = set2.difference(set1)
# # print(set3)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)


# set_1 = {"red", "brown", "orange", "burgundy"}
# set_2 = {"blue", "green", "red", "purple", "brown", "yellow"}
# set_3 = {"violet", "indigo", "peach", "pink", "red"}

# print(set_1.difference(set_2).difference(set_3))
# print(set_1 - set_2 - set_3)


# -----------------------------DIFFERENCE OF SETS------------------------------


# -----------------------------SYMMETRIC DIFFERENCE OF SETS------------------------------

# set_1 = {"red", "brown", "orange", "burgundy"}
# set_2 = {"blue", "green", "red", "purple", "brown", "yellow"}

# print(set_1.symmetric_difference(set_2))

# union = set_1.union(set_2)
# intersection = set_1.intersection(set_2)

# symmetric_diff = union - intersection

# print(symmetric_diff)

# print(set_1 ^ set_2)

# set_1.symmetric_difference_update(set_2)
# print(set_1)


# -----------------------------SYMMETRIC DIFFERENCE OF SETS------------------------------


# -----------------------------REMOVING FROM SETS------------------------------

# set_1 = {"red", "brown", "orange", "burgundy"}

# # set_1.remove("red")
# # set_1.discard("red")

# # set_1.remove("blue")
# set_1.discard("blue")

# print(set_1)

# -----------------------------REMOVING FROM SETS------------------------------



# set_1 = {"red", "brown", "orange", "burgundy"}
# set_2 = {"blue", "green", "red", "purple", "brown", "yellow"}
# print(set_1.isdisjoint(set_2))



# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {1, 2, 3}
# set_3 = {3, 4, 5}
# set_4 = {7, 4, 5}

# print(set_2.issubset(set_1))
# print(set_3.issubset(set_1))
# print(set_4.issubset(set_1))
# print(set_1.issuperset(set_2))
# print(set_1.issuperset(set_4))



