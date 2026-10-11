import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

print("\n========== Q1: EXPLORATORY DATA ANALYSIS ==========")

employees = {"Emp_ID": list(range(101, 121)),
    "Name": ["Aarav", "Diya", "Rohan", "Priya", "Karan","Neha", "Jay", "Mira", "Dev", "Riya","Arjun", "Isha", "Krish", "Pooja", "Rahul","Anaya", "Vivek", "Nisha", "Manav", "Tara"],
    "Department": ["IT", "HR", "Sales", "IT", "Finance","HR", "Sales", "IT", "Finance", "Sales","IT", "HR", "Finance", "Sales", "IT","HR", "Sales", "Finance", "IT", "HR"],
    "Salary": [30000, 35000, 28000, 45000, 40000,32000, 38000, 50000, 42000, 36000,55000, 33000, 48000, 39000, 60000,37000, 41000, 52000, 65000, 34000],
    "Experience": [1, 2, 1, 4, 3, 2, 3, 5, 4, 2,6, 2, 5, 3, 7, 3, 4, 6, 8, 2]
    }

df = pd.DataFrame(employees)

# df.to_csv("employees.csv", index=False)

# df = pd.read_csv("employees.csv")
df = pd.DataFrame(employees)

print(df)

print(df.head())

print(df.info())

print(df.shape)

print(df.describe())

print(df.isnull().sum())

# df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

print("Mean:", df["Salary"].mean())
print("Median:", df["Salary"].median())
print("Mode:", df["Salary"].mode().tolist())
print("Variance:", df["Salary"].var())
print("Standard Deviation:", df["Salary"].std())

# Salary histogram
plt.hist(df["Salary"], bins=6, edgecolor="black")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Univariate Analysis: Salary Distribution")
plt.show()

# Step 9: Bivariate analysis
plt.scatter(df["Experience"], df["Salary"])
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()

# Step 10: Multivariate correlation analysis
numeric_df = df.select_dtypes(include=np.number)
correlation_matrix = numeric_df.corr()

print("\n--- Correlation Matrix ---")
print(correlation_matrix)

sns.heatmap(correlation_matrix,annot=True,
    cmap="coolwarm",
    fmt=".2f")
plt.title("Employee Numerical Correlation Heatmap")
plt.show()



# ========================================================================================================================

data = {
    "House_Size": [850, 900, 1000, 1100, 1200,1300, 1400, 1500, 1600, 1700,1800, 1900, 2000, 2100, 2200],
    "Price": [75, 80, 85, 88, 90,95, 100, 110, 115, 120,125, 130, 135, 140, 150]
}

house_df = pd.DataFrame(data)
print(house_df)

X = house_df[["House_Size"]]
y = house_df["Price"]

print("\nIndependent",X.columns.tolist())
print("Dependent",y.name)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=42)

print(X_train)
print(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

print(f"Equation: Price = {model.coef_[0]:.4f}"
    f" * House_Size + {model.intercept_:.4f}")

y_pred = model.predict(X_test)

results = pd.DataFrame({
    "House_Size": X_test["House_Size"].values,
    "Actual_Price": y_test.values,
    "Predicted_Price": np.round(y_pred, 2)
})

print(results.to_string(index=False))

r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)
rmse = np.sqrt(mse)
print("RMSE:", rmse)

plt.scatter(X,y,label="Actual Data")
plt.plot(X,model.predict(X),color="red", label="Regression Line")
plt.xlabel("House Size (Square Feet)")
plt.ylabel("Price (Dataset Units)")
plt.title("House Size vs House Price")
plt.legend()
plt.show()

# Step 10: Predict price for a new house
new_house = pd.DataFrame({"House_Size": [1800]})
new_price = model.predict(new_house)
