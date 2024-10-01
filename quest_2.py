import pandas as pd
import matplotlib.pyplot as plt

#  Write a Python program to create a Pie plot to get the frequency of the three species of the Iris data. (Use iris.csv)

# Step 1: Load the Iris dataset
df = pd.read_csv('iris.csv')

# Step 2: Count the occurrences of each species
species_count = df['species'].value_counts()
# print(species_count)

# Step 3: Create a pie plot
plt.pie(species_count, labels=species_count.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'])

# Add a title
plt.title('Frequency of Iris Species')

# Display the pie chart
plt.show()


#  Write a Python program to generate a line plot of name vs salary.
# df = pd.read_csv('employee.csv')
# plt.plot(df['name'], df['salary'], label='line plot', marker='o' ,color='crimson')
# plt.xlabel('name')
# plt.xlabel('salary')
# plt.title('id vs salary')
# plt.show()


#  Write a Python program to create box plots to see how each feature (i.e., Sepal Length, Sepal Width, Petal Length, Petal Width) is distributed across the three species. (Use iris.csv dataset)

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Step 1: Load the Iris dataset
# df = pd.read_csv('iris.csv')

# # Step 3: Create box plots for each feature
# # Sepal Length
# plt.subplot(2, 2, 1)
# sns.boxplot(x='species', y='sepal_length', data=df)
# plt.title('Sepal Length Distribution by Species')

# # Sepal Width
# plt.subplot(2, 2, 2)
# sns.boxplot(x='species', y='sepal_width', data=df)
# plt.title('Sepal Width Distribution by Species')

# # Petal Length
# plt.subplot(2, 2, 3)
# sns.boxplot(x='species', y='petal_length', data=df)
# plt.title('Petal Length Distribution by Species')

# # Petal Width
# plt.subplot(2, 2, 4)
# sns.boxplot(x='species', y='petal_width', data=df)
# plt.title('Petal Width Distribution by Species')

# plt.show()




#  Generate a random array of 50 integers and display them using a line chart, scatter plot, histogram, and box plot. Apply appropriate color, labels, and styling options.

# import numpy as np

# # Generate a random array of 50 integers
# random_data = np.random.randint(0, 100, size=50)
# indices = np.arange(1, 51)

# plt.subplot(2,2,1)
# plt.plot(random_data, marker='o', color='royalblue')
# plt.xlabel('index')
# plt.ylabel('value')
# plt.title('line chart')

# plt.subplot(2,2,2)
# plt.scatter(indices, random_data, marker='o', color='crimson')
# plt.xlabel('index')
# plt.ylabel('value')
# plt.title('scatter plot')

# plt.subplot(2,2,3)
# plt.hist(random_data, bins=5, color='purple', edgecolor='black')
# plt.xlabel('index')
# plt.ylabel('value')
# plt.title('histogram')

# plt.subplot(2,2,4)
# plt.boxplot(random_data)
# plt.title('boxplot')

# plt.tight_layout()
# plt.show()


#  Write a Python program to generate a line plot of name vs salary.
# df = pd.read_csv('employee.csv')
# plt.plot(df['name'], df['salary'], marker='o', color='salmon')
# plt.xlabel('name')
# plt.ylabel('salary')
# plt.title('name vs salary line plot')
# plt.show()


#  Write a Python program to display column-wise mean and median for the SOCR-HeightWeight dataset.

# df = pd.read_csv('employee.csv')
# print(df[['height', 'weight']].mean())
# print(df[['height', 'weight']].median())




#  Write a Python program to create a Pie plot to get the frequency of the three species of the Iris data. (Use iris.csv)
# df = pd.read_csv('iris.csv')
# species = df['species'].value_counts()
# plt.pie(species, data=df, labels=species.index, autopct='%1.1f%%', colors=['red', 'yellow', 'green'])
# plt.title('pie chart of species')
# plt.legend()
# plt.show()



#  Write a Python program to create a graph to find the relationship between petal length and petal width. (Use iris.csv dataset)
# import seaborn as sns

# # Step 1: Load the Iris dataset
# df = pd.read_csv('iris.csv')

# sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=df)

# # Step 3: Add labels and title
# plt.xlabel('Petal Length (cm)')
# plt.ylabel('Petal Width (cm)')
# plt.title('Scatter Plot of Petal Length vs Petal Width')

# # Step 4: Display the plot
# plt.show()





#  Write a Python program to generate a random array of 50 integers and display them using a line chart, scatter plot, histogram, and box plot. Apply appropriate color, labels, and styling options.

# import numpy as np

# data = np.random.randint(1, 100, 50)
# indices = np.arange(1, 51)
# plt.subplot(2,2,1)
# plt.plot(data, marker='o', color='yellow', linestyle='-')
# plt.xlabel('index')
# plt.ylabel('values')
# plt.title('line chart')

# plt.subplot(2,2,2)
# plt.scatter(indices, data, marker='o', color='royalblue')
# plt.xlabel('index')
# plt.ylabel('values')
# plt.title('scatter plot')

# plt.subplot(2,2,3)
# plt.hist(data, bins=5, color='lightseagreen', edgecolor='black')
# plt.xlabel('index')
# plt.ylabel('values')
# plt.title('histogram')

# plt.subplot(2,2,4)
# plt.boxplot(data)
# plt.xlabel('index')
# plt.ylabel('values')
# plt.title('box plot')

# plt.tight_layout()
# plt.show()



# Write a Python program to create two lists, one representing subject names and the other representing marks obtained in those subjects. Display the data in a pie chart and bar chart.
# subjects = ['Math', 'Science', 'English', 'History', 'Art']
# marks = [85, 90, 78, 88, 95]

# plt.subplot(1,2,1)
# plt.pie(marks, labels=subjects, autopct='%1.1f%%', colors=['crimson', 'lightseagreen', 'salmon', 'royalblue', 'purple'])
# plt.title('Marks in pie chart')

# plt.subplot(1,2,2)
# plt.bar(subjects, marks, color='lightcoral', edgecolor='black')
# plt.xlabel('subjects')
# plt.ylabel('marks')
# plt.title('Marks in bar chart')

# plt.tight_layout()
# plt.show()



#  Write a Python program to draw scatter plots to compare two features of the Iris dataset.

# import seaborn as sns

# df = pd.read_csv('iris.csv')
# sns.scatterplot(x=df['sepal_length'], y=df['sepal_width'], hue='species', data=df)
# plt.xlabel('sepal_length')
# plt.ylabel('sepal_width')
# plt.title('scatter plot')
# plt.show()



#  Write a Python program to create box plots to see how each feature (i.e., Sepal Length, Sepal Width, Petal Length, Petal Width) is distributed across the three species. (Use iris.csv dataset)

# df = pd.read_csv('iris.csv')

# plt.subplot(2,2,1)
# plt.boxplot(df['sepal_length'])
# plt.title('sepal_length')

# plt.subplot(2,2,2)
# plt.boxplot(df['sepal_width'])
# plt.title('sepal_width')

# plt.subplot(2,2,3)
# plt.boxplot(df['petal_length'])
# plt.title('petal_length')

# plt.subplot(2,2,4)
# plt.boxplot(df['petal_width'])
# plt.title('petal_width')

# plt.tight_layout()
# plt.show()



#  Add two outliers to the above data and display the box plot.
# import seaborn as sns

# # Step 1: Load the Iris dataset
# df = pd.read_csv('iris.csv')

# # Step 2: Add two outliers to sepal_length and sepal_width
# outliers = pd.DataFrame({
#     'sepal_length': [15, 16],  # Adding outliers for Sepal Length
#     'sepal_width': [0.5, 0.3],  # Adding outliers for Sepal Width
#     'petal_length': [1.4, 1.5],  # Keeping petal_length and petal_width reasonable
#     'petal_width': [0.2, 0.3],
#     'species': ['setosa', 'versicolor']  # Random species for outliers
# })

# # Append outliers to the original dataset
# df_with_outliers = df.append(outliers, ignore_index=True)


# # Box plot for Sepal Length
# plt.subplot(1, 2, 1)
# sns.boxplot(x='species', y='sepal_length', data=df_with_outliers)
# plt.title('Box Plot of Sepal Length with Outliers')

# # Box plot for Sepal Width
# plt.subplot(1, 2, 2)
# sns.boxplot(x='species', y='sepal_width', data=df_with_outliers)
# plt.title('Box Plot of Sepal Width with Outliers')

# # Step 4: Display the plots
# plt.tight_layout()
# plt.show()




#  Import dataset “iris.csv”. Write a Python program to create a bar plot to get the frequency of the three species of the Iris data.
# import seaborn as sns
# df = pd.read_csv('iris.csv')
# species = df['species'].value_counts()

# sns.barplot(x=species.index, y=species.values)
# plt.title('three species')

# plt.show()



# Write a Python program to create a histogram of the three species of the Iris data.
# import seaborn as sns

# df = pd.read_csv('iris.csv')

# sns.histplot(data=df, x='sepal_length', hue='species')

# # Step 3: Add labels and title
# plt.xlabel('Sepal Length (cm)')
# plt.ylabel('Density')
# plt.title('Histogram of Sepal Length by Species')

# # Step 4: Display the plot
# plt.show()



