import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.bar(['Electronics', 'Clothing', 'Home'],[300, 450, 200])
plt.title("Bar Chart")
plt.xlabel('Categories')
plt.ylabel('Values')

plt.subplot(1,2,2)
plt.plot(['Electronics', 'Clothing', 'Home'],[300, 450, 200])
plt.title("Line Plot")
plt.xlabel('Categories')
plt.ylabel('Values')

plt.tight_layout()
plt.show()
