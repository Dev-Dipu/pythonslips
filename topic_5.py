import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Load the dataset
data = {
    'Gender': ['Male', 'Female', 'Female', None, 'Male'],
    'Height': [73, 62, None, 60, 70],
    'Weight': [241, 150, 130, 120, None]
}
df = pd.DataFrame(data)

# Step 2: Handle missing values
imputer = SimpleImputer(strategy='mean')
df['Height'] = imputer.fit_transform(df[['Height']])
df['Weight'] = imputer.fit_transform(df[['Weight']])

# Step 3: Encode categorical data
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'].astype(str))  # Convert None to string

# Step 4: Scale the features
scaler = StandardScaler()
df[['Height', 'Weight']] = scaler.fit_transform(df[['Height', 'Weight']])

# Step 5: Split the data into training and testing sets
X = df[['Gender', 'Height', 'Weight']]
y = [1, 0, 0, 0, 1]  # Example target variable (0: No, 1: Yes)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the preprocessed data
print("Preprocessed DataFrame:")
print(df)
print("\nTraining Features:")
print(X_train)
print("\nTesting Features:")
print(X_test)
