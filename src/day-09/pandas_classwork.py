import pandas as pd
s1 = pd.Series([10,20,30,40])
s2 = pd.Series([10,20,30], index = ['a','b','c'])
print(s1)
print(s2)

print(s2['a'])
print(s2[['a','c']])


scores = pd.Series([10,20,30,40,50])
print(scores[scores>30])

scores1 = pd.Series([10,None,30,None,50])
print(scores1.isnull())
print(scores1.fillna(0))

char = pd.Series(['Alice','bob','ABHISHEK'])
char1 = char.str.lower()
print(char1)
print(char1.str.contains('a'))