# TASK 1 (creating lists and using append(), remove(), and sort())
print("\nTASK 1 (creating lists and using append(), remove(), and sort())")
inventory = ["Apples","Bananas","Carrots","Dates"]
print(inventory)

inventory.append("Eggs")
print(inventory)

inventory.remove("Bananas")
print(inventory)

inventory.sort()
print(inventory)


# TASK 2 (Goal: Master zero-based indexing and slicing ranges.)
print("\nTASK 2 (Goal: Master zero-based indexing and slicing ranges.)")
temperatures=[22,24,25,28,30,29,27,26,24,22]
print("First Reading is",temperatures[0],"and Last Reading is ",temperatures[-1])
print("Afternoon Peak readings are : ",temperatures[3:6])
print("the Last 3 Hours are : ",temperatures[-3:])


#TASK 3 (Goal: Understand why Tuples cannot be changed (Immutability).)
print("\nTASK 3 (Goal: Understand why Tuples cannot be changed (Immutability).)")
screen_res = (1920,1080)
print("Current Resolution : ",screen_res[0],"X",screen_res[1])
screen_res[0]=1280
print(screen_res) 