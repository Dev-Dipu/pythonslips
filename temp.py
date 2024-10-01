import pandas as pd
import matplotlib.pyplot as plt

#  Write a Python program to create a Pie plot to get the frequency of the three species of the Iris data. (Use iris.csv)

# df = pd.read_csv('iris.csv')
# species = df['species'].value_counts()

# plt.pie(species, labels=species.index, autopct='%1.1f%%', colors=['red', 'aqua', 'lightseagreen'])
# plt.title('pie plot')
# plt.legend()
# plt.show()

#  Write a Python program to generate a line plot of name vs salary.

# df = pd.read_csv('employee.csv')

# plt.plot(df['name'], df['salary'], color='orange', marker='o')
# plt.xlabel('name')
# plt.ylabel('salary')
# plt.title('name vs salary')
# plt.show()

# Write a Python program to create box plots to see how each feature (i.e., Sepal Length, Sepal Width, Petal Length, Petal Width) is distributed across the three species. (Use iris.csv dataset)

# import seaborn as sns

# df = pd.read_csv('iris.csv')

# plt.subplot(2,2,1)
# sns.boxplot(x = 'species', y = 'sepal_length', data=df)
# plt.title('sepal length box plot')

# plt.subplot(2,2,2)
# sns.boxplot(x = 'species', y = 'sepal_width', data=df)
# plt.title('sepal width box plot')

# plt.subplot(2,2,3)
# sns.boxplot(x = 'species', y = 'petal_length', data=df)
# plt.title('petal length box plot')

# plt.subplot(2,2,4)
# sns.boxplot(x = 'species', y = 'petal_width', data=df)
# plt.title('petal width box plot')
# plt.tight_layout()
# plt.show()



#  Generate a random array of 50 integers and display them using a line chart, scatter plot, histogram, and box plot. Apply appropriate color, labels, and styling options.

# import numpy as np

# data = np.random.randint(1, 100, 50)
# indices = np.arange(1,51)

# plt.subplot(2,2,1)
# plt.plot(data, marker='o', color='crimson')
# plt.xlabel('index')
# plt.ylabel('random data')
# plt.title('line chart')

# plt.subplot(2,2,2)
# plt.scatter(data, indices, color='green')
# plt.xlabel('index')
# plt.ylabel('random data')
# plt.title('scatter plot')

# plt.subplot(2,2,3)
# plt.hist(data, bins=5, color='purple', edgecolor='black')
# plt.xlabel('index')
# plt.ylabel('random data')
# plt.title('histogram')

# plt.subplot(2,2,4)
# plt.boxplot(data)
# plt.xlabel('index')
# plt.ylabel('random data')
# plt.title('box plot')
# plt.tight_layout()
# plt.show()


