# # Task 01
# Name = input("Enter Your Name : ")
# daily_Goal = input("Enter your Daily Goal : ")
# file = open("journal.txt","a")
# file.write("Name : " + Name)
# file.write("\nDaily Goal :" + daily_Goal + "\n")
# file.write("\n")
# file.close()

# # TASK 02
# import csv
# with open('students.csv','w', newline='') as csv_file:
#     write = csv.writer(csv_file)
#     write.writerow(['Name','Grade','Status'])
#     write.writerow(['Alice','A','Pass'])
#     write.writerow(['Bob','B','Pass'])
#     write.writerow(['Charlie','F','Fail'])

# with open('students.csv','r') as csv_read:
#     reads = csv.reader(csv_read)
#     for row in reads:
#         if row[2] == "Pass":
#             print(row[0])

#TASK 03
filename = input("Enter the File Name (write only file name without Extension) : ")

try :
    file = open(f'{filename}.txt','r') 
    readers = file.read()
    print(readers)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")