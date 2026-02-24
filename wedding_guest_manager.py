# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 2

waitlist.extend(["Ken", "Jack", "Ivy"])
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 3

waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 4

confirmed_guests.remove("Alice")
confirmed_guests.insert(0, waitlist[0])
waitlist.pop(0)
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 5

check_charlie = "Charlie" in confirmed_guests
print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"It is {check_charlie} that Charlie is in the guest list")


# Stage 6
confirmed_guests.pop(6)
del confirmed_guests[2] 
# del confirmed_guests[5]
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 7
confirmed_guests.insert(2, waitlist[0])
waitlist.pop(0)
confirmed_guests.insert(6, waitlist[0])
del waitlist[0]
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 8
waitlist.remove("Oliver")
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 9
print("\n\nStage 9")
print(confirmed_guests[-3:])
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 10
confirmed_guests.append(waitlist[0])
waitlist.remove("Noah")
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 11
print("\n\nStage 10")
print(len(confirmed_guests))
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)