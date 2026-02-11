#TASK 01
import pandas as pd
products = pd.Series([700,150,300],index = ['Laptop','Mouse', 'Keyword'])
laptop_price = products['Laptop']
print("Laptop Price :", laptop_price)
print("first two products using positional indexing : \n",products[['Laptop','Mouse']])
print("\nProducts List :\n",products)

#TASK 02
grades = pd.Series([85, None, 92, 45, None, 78, 55])
null_values = grades.isnull()
filled_series = grades.fillna(0)
filtered_results = grades[grades > 60]
print(f'Original Series : \n{grades}\n')
print(f'Filled Series : \n{filled_series}\n')
print(f'Filtered Results : \n{filtered_results}\n')

#TASK 03
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print(usernames.str.strip())
print(usernames.str.lower())
print(usernames.str.contains('a'))
print(f'Cleaned Series : \n{usernames.str.lower()}\n')
print(f'boolean result of the a search : \n{usernames.str.contains('a')}')