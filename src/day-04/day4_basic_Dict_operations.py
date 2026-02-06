Students={
    "name":"Abhishek",
    "age":21,
    "location":"Mangalore"
}
print(f'Name : {Students["name"]} \nAge : {Students["age"]} \nLocation : {Students["location"]}')


for subject,score in Students.items():
    print(subject,score)
print(len(Students))

Students.update(degree="BE")
Students.pop("name")
print(Students)



#Creating the dictionary using User input
count=int(input("Enter the number of the Students : "))
students_details={}

for i in range(count):
    print(f'Enter the {i+1}th details')
    stud_name=input("Enter your name : ")
    stud_class=int(input(f'Enter your currently pursuing Standard for {stud_name} : '))
    students_details[stud_name]=stud_class
print(students_details)

junior = min(students_details , key = students_details.get)
print(f'Junior : {junior}')
senior = max(students_details , key = students_details.get)
print(f'Senior : {senior}')