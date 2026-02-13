import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.bar(x,y)
plt.title("Bar Chart")

plt.subplot(2, 2, 3)
plt.hist(x,y)
plt.title("Histogram Chart")
plt.show()

cate = ['A','B','C','D']
vals = [6,4,3,2]
plt.bar(cate,vals)
plt.title('Bar Graph')
plt.show()
plt.scatter(x,y)
plt.show()