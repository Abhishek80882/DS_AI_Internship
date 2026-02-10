import numpy as np

#Sum of the TWO arrays with one array
a= np.array([[[1,2,3],[4,5,6],[7,8,9]]])
b=np.array([2,4,6])
print(a+b)

#Sum of the TWO arrays with one element (1-D array)
c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
d = np.array(1)
print("\n",c+d,"\n")

# Vectorisation...
arr = np.random.randint(range(50,100))
print(arr,"\n")

# Re-Shape
ranges = np.arange(9)
reshaped = ranges.reshape(3,3)
print(reshaped)

# Stacking
x=np.array([[1,2,3],[7,8,9]])
y=np.array([4,5,6])
print(np.vstack((x,y)))
print(np.hstack((b,y)))

# Statistics
arr = np.array([[1,2,3],[4,5,6]])
print(np.mean(arr))
print(np.mean(arr,axis=1))
print(np.mean(arr,axis=0))

# Matrix Multiplication
m = np.array([[3,4,5],[8,7,6]])
n = np.array([[1,2,3],[5,4,3]])
print("Matrix Multiplication : \n",m*n)

#Writing the 3-D array
s = np.array([[[1,2,3],[4,5,6]],[[1,3,5],[5,7,3]]])
print(s)

arr1 = [1,2,3,4,5,6]
print(np.linspace(0,3))
print(np.random.uniform(3,2))











