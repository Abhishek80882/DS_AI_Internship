#TASK-1
name=input("Enter your name : ")
age=int(input("Enter your Age : "))

new_age=age+4
print(f'Hey {name}, you will be {new_age} years old in 2030')

#TASK-2
Amount = float(input("Enter the Total Bill Amount : "))
People =int(input("Enter the number of the peoples : "))
share=Amount/People
print(f'Total Bill : {Amount}. Each person pays: {share:.2f}')

#TASK-3
item_name="Mobile"
quantity=4
price=1999.98
in_stock=True

print("item:",item_name,", Qty:",quantity,", Price:",price,", Available:",in_stock)
total_cost=quantity*price
print("Total Cost: ",total_cost)