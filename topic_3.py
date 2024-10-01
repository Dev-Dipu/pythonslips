import pandas as pd

# Step 1: Load your dataset
data = {
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'],
    'Marks': [85, 90, 78, 88, 95]
}
df = pd.DataFrame(data)

temp = df.value_counts()
print(temp, temp.index, temp.values)

# Step 2: Calculate Mean
mean_marks = df['Marks'].mean()
print(f"Mean of Marks: {mean_marks}")

# Step 3: Calculate Median
median_marks = df['Marks'].median()
print(f"Median of Marks: {median_marks}")

# Step 4: Calculate Minimum and Maximum
min_marks = df['Marks'].min()
max_marks = df['Marks'].max()
print(f"Minimum Marks: {min_marks}")
print(f"Maximum Marks: {max_marks}")

# Step 5: Calculate Standard Deviation and Variance
std_dev = df['Marks'].std()
variance = df['Marks'].var()
print(f"Standard Deviation of Marks: {std_dev}")
print(f"Variance of Marks: {variance}")
