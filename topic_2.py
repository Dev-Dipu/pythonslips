import matplotlib.pyplot as plt

# # Example Data
# x = [1, 2, 3, 4, 5]
# y = [10, 14, 12, 17, 15]

# # Create a line plot
# plt.plot(x, y, label='Line Chart', color='blue')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Line Chart')
# plt.legend()

# # Show the plot
# plt.show()


# # Example Data
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# # Create a scatter plot
# plt.scatter(x, y, label='Scatter Plot', color='green')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Scatter Plot')
# plt.legend()

# # Show the plot
# plt.show()


# # Example Data
# data = [22, 55, 62, 45, 21, 22, 34, 42, 35, 50, 60, 75, 80, 85, 90]

# # Create a histogram
# plt.hist(data, bins=5, color='purple', edgecolor='black')
# plt.xlabel('Value Range')
# plt.ylabel('Frequency')
# plt.title('Simple Histogram')

# # Show the plot
# plt.show()


# # Example Data
# data = [22, 55, 62, 45, 21, 34, 42, 35, 50, 60, 75, 80, 85, 90]

# # Create a box plot
# plt.boxplot(data)
# plt.title('Simple Box Plot')

# # Show the plot
# plt.show()



import seaborn as sns

# Load an example dataset
df = sns.load_dataset('iris')

# # Create a scatter plot
# sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')

# plt.title('Scatter Plot with Seaborn')
# plt.show()


# # Box plot showing the distribution of sepal length across species
# sns.boxplot(x='species', y='sepal_length', data=df)
# plt.title('Box Plot with Seaborn')
# plt.show()


# # Create a pair plot
# sns.pairplot(df, hue='species')
# plt.show()


