import pandas as pd

# Write a Python program to create a DataFrame containing columns name, age, salary, department. Add 10 rows to the DataFrame. View the DataFrame.
# # Step 1: Create a DataFrame with specified columns
# data = {
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 
#              'Frank', 'Grace', 'Hannah', 'Ian', 'Judy'],
#     'age': [25, 30, 35, 40, 28, 
#             22, 27, 34, 31, 29],
#     'salary': [50000, 60000, 55000, 70000, 48000, 
#                52000, 61000, 67000, 72000, 53000],
#     'department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 
#                    'HR', 'IT', 'Finance', 'Marketing', 'Sales']
# }

# # Step 2: Create the DataFrame
# df = pd.DataFrame(data)

# # Step 3: View the DataFrame
# print("DataFrame:")
# print(df)




#  Write a Python program to create two lists, one representing subject names and the other representing marks obtained in those subjects. Display the data in a pie chart and bar chart.
# import matplotlib.pyplot as plt

# subjects = ['Math', 'Science', 'English', 'History', 'Art']
# marks = [85, 90, 78, 88, 95]

# plt.pie(marks, labels=subjects, autopct='%1.1f%%', colors=['crimson', 'salmon', 'purple', 'royalblue', 'lightseagreen'])
# plt.title('Marks pie chart')
# plt.legend()
# plt.show()
