# #TASK 01
# print("TASK 01: Goal: Practice dictionary creation, updating, and safe data retrieval using .get().")
# Contacts = {
#     "Abhi":123456789,
#     "Avinash":147852369,
#     "hemu":789654123
# }
# Contacts.update(kumar=1265897)
# print(Contacts)
# Existence = Contacts.get("Abhi","Contact not Found")
# missing = Contacts.get("manu","Contact not Found")
# print(Existence)
# for name,number in Contacts.items():
#     print(f'Contact: {name} | Phone: {number}.')


# #TASK 2
# print("\nTASK 02: Goal: Understand how sets handle uniqueness and perform membership testing.")
# IDs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
# unique_users=set(IDs)
# print("Origin List:",IDs)
# print("Set : ",unique_users)
# print(f'Existed in Set: {"ID05" in unique_users}')
# original_length=len(IDs)
# set_length=len(unique_users)
# duplicates_removed=original_length-set_length
# print("Duplicated Values removed in the set:",duplicates_removed)



#TASK 3
print("\nTASK 03: Goal: Use mathematical set operations (Intersection and Union) to find commonalities.")
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(f'Intersection :  {friend_a & friend_b}')
print(f'Union        :  {friend_a | friend_b}')
print(f'Difference   :  {friend_a - friend_b}')
