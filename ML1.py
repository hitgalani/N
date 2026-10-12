
# ============================================================
# FUNDAMENTALS OF MACHINE LEARNING
# SYBCA-AI SEMESTER III
# ALL 5 PRACTICALS IN ONE PYTHON FILE
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)


# ============================================================
# PRACTICAL 1: EMPLOYEE CSV FILE AND EXPLORATORY DATA ANALYSIS
# ============================================================

def practical_1():
    # Create employees.csv with 20 records
    data = {
        "Emp_ID": list(range(101, 121)),
        "Name": [
            "Amit", "Riya", "Rahul", "Neha", "Karan",
            "Priya", "Jay", "Mira", "Raj", "Anita",
            "Vijay", "Pooja", "Dev", "Kavya", "Arjun",
            "Nisha", "Rohan", "Meera", "Harsh", "Diya"
        ],
        "Department": [
            "IT", "HR", "Sales", "IT", "Finance",
            "HR", "IT", "Sales", "Finance", "IT",
            "HR", "Sales", "IT", "Finance", "Sales",
            "IT", "HR", "Finance", "Sales", "IT"
        ],
        "Salary": [
            30000, 35000, 40000, 45000, 50000,
            32000, 55000, 38000, 60000, 48000,
            36000, 42000, 65000, 52000, 44000,
            70000, 39000, 58000, 46000, 75000
        ],
        "Experience": [
            1, 2, 3, 4, 5, 2, 6, 3, 7, 4,
            2, 3, 8, 5, 4, 9, 3, 6, 4, 10
        ]
    }

    df = pd.DataFrame(data)

    # Save dataset to CSV
    df.to_csv("employees.csv", index=False)
    print("employees.csv created successfully.")

    # Load the CSV file
    df = pd.read_csv("employees.csv")

    # Display first 5 rows
    print("\nFirst 5 Records:")
    print(df.head())

    # Dataset information
    print("\nDataset Information:")
    df.info()

    # Univariate analysis of Salary
    print("\nSalary Analysis")
    print("Mean:", df["Salary"].mean())
    print("Median:", df["Salary"].median())
    print("Mode:", df["Salary"].mode()[0])
    print("Variance:", df["Salary"].var())
    print("Standard Deviation:", df["Salary"].std())

    # Histogram
    plt.figure(figsize=(7, 5))
    plt.hist(df["Salary"], bins=8, edgecolor="black")
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Number of Employees")
    plt.grid(True)
    plt.show()

    # Bivariate analysis
    plt.figure(figsize=(7, 5))
    plt.scatter(df["Experience"], df["Salary"])
    plt.title("Experience vs Salary")
    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.grid(True)
    plt.show()

    # Multivariate analysis
    print("\nCorrelation Matrix:")
    correlation = df.corr(numeric_only=True)
    print(correlation)

    plt.figure(figsize=(7, 5))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Handle missing values
    df["Salary"] = df["Salary"].fillna(df["Salary"].median())
    df["Experience"] = df["Experience"].fillna(
        df["Experience"].median()
    )
    df["Name"] = df["Name"].fillna(df["Name"].mode()[0])
    df["Department"] = df["Department"].fillna(
        df["Department"].mode()[0]
    )

    print("\nMissing Values After Handling:")
    print(df.isnull().sum())


# ============================================================
# PRACTICAL 2: HOUSE PRICE PREDICTION USING LINEAR REGRESSION
# ============================================================

def practical_2():
    data = {
        "House_Size": [
            850, 900, 1000, 1100, 1200,
            1300, 1400, 1500, 1600, 1700,
            1800, 1900, 2000, 2100, 2200
        ],
        "Price": [
            75, 80, 85, 88, 90,
            95, 100, 110, 115, 120,
            125, 130, 135, 140, 150
        ]
    }

    df = pd.DataFrame(data)

    # Display dataset
    print("Dataset:")
    print(df)

    # Independent and dependent variables
    X = df[["House_Size"]]
    Y = df["Price"]

    # Split into training and testing data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.20, random_state=42
    )

    print("\nTraining Data:")
    print(X_train)

    print("\nTesting Data:")
    print(X_test)

    # Create and train model
    model = LinearRegression()
    model.fit(X_train, Y_train)

    # Display coefficient and intercept
    print("\nCoefficient:", model.coef_[0])
    print("Intercept:", model.intercept_)

    print(
        "Regression Equation: Price =",
        model.coef_[0], "* House_Size +", model.intercept_
    )

    # Predict test data
    Y_pred = model.predict(X_test)

    print("\nActual vs Predicted Price:")
    result = pd.DataFrame({
        "House_Size": X_test["House_Size"],
        "Actual_Price": Y_test,
        "Predicted_Price": Y_pred
    })
    print(result)

    # Evaluate model
    print("\nModel Performance")
    print("R2 Score:", r2_score(Y_test, Y_pred))
    print("Mean Squared Error:", mean_squared_error(Y_test, Y_pred))
    print("Mean Absolute Error:", mean_absolute_error(Y_test, Y_pred))

    # Plot regression line
    plt.figure(figsize=(7, 5))
    plt.scatter(X["House_Size"], Y, label="Actual Data")
    plt.plot(
        X["House_Size"], model.predict(X),
        label="Regression Line"
    )
    plt.title("House Size vs House Price")
    plt.xlabel("House Size (sq. ft.)")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()


# ============================================================
# PRACTICAL 3: SPAM CLASSIFICATION USING LOGISTIC REGRESSION
# ============================================================

def practical_3():
    # Dataset from the practical
    SuspiciousWords = [
        [0], [1], [1.5], [2], [2.5],
        [3], [3.5], [4], [5], [6]
    ]

    Result = [
        "Not Spam", "Not Spam", "Not Spam", "Not Spam",
        "Not Spam", "Spam", "Spam", "Spam", "Spam", "Spam"
    ]

    # Convert labels to 0 and 1
    y = [1 if x == "Spam" else 0 for x in Result]
    X = SuspiciousWords

    # Display dataset
    df = pd.DataFrame({
        "Suspicious_Words": [x[0] for x in X],
        "Result": Result,
        "Encoded_Result": y
    })

    print("Dataset:")
    print(df)

    # Scatter plot
    plt.scatter([x[0] for x in X], y)
    plt.xlabel("Number of Suspicious Words")
    plt.ylabel("Result (0 = Not Spam, 1 = Spam)")
    plt.title("Suspicious Words vs Spam Email")
    plt.grid(True)
    plt.show()

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create and train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict test data
    y_pred = model.predict(X_test)

    print("\nActual Results:", y_test)
    print("Predicted Results:", y_pred)

    # Predict email with 4 suspicious words
    prediction = model.predict([[4]])
    print("\nPrediction for 4 suspicious words:", prediction[0])

    if prediction[0] == 1:
        print("Email is Spam.")
    else:
        print("Email is Not Spam.")

    # Prediction probabilities
    prob = model.predict_proba([[4]])

    print("\nPrediction Probabilities:")
    print("Probability of Not Spam:", prob[0][0])
    print("Probability of Spam:", prob[0][1])


# ============================================================
# COMMON DATASET FOR PRACTICAL 4 AND PRACTICAL 5
# ============================================================

def create_student_data():
    data = {
        "Study_Hours": [
            2, 3, 3, 4, 4, 5, 5, 6, 6, 6,
            7, 7, 7, 8, 8, 8, 9, 9, 9, 10,
            3, 4, 5, 6, 7, 8, 9, 10, 5, 7
        ],
        "Attendance": [
            55, 60, 65, 62, 68, 70, 73, 75, 78, 80,
            82, 85, 88, 90, 92, 94, 96, 97, 98, 99,
            58, 66, 72, 76, 84, 89, 95, 98, 74, 86
        ],
        "Marks": [
            40, 45, 50, 55, 58, 62, 65, 68, 70, 73,
            75, 78, 80, 82, 84, 86, 88, 90, 92, 95,
            48, 57, 63, 69, 77, 83, 89, 94, 67, 79
        ]
    }

    df = pd.DataFrame(data)

    def grade(marks):
        if marks >= 85:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"

    df["Grade"] = df["Marks"].apply(grade)
    return df


# ============================================================
# PRACTICAL 4: MULTICLASS CLASSIFICATION USING ONE-VS-REST
# ============================================================

def practical_4():
    df = create_student_data()

    # Display dataset
    print("Student Dataset:")
    print(df)

    # Independent and dependent variables
    X = df[["Study_Hours", "Attendance"]]
    y = df["Grade"]

    # Split data using stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Logistic Regression with One-vs-Rest
    log_model = LogisticRegression(max_iter=1000)
    model = OneVsRestClassifier(log_model)

    # Train model
    model.fit(X_train, y_train)

    # Predict test data
    y_pred = model.predict(X_test)

    # Display actual and predicted grades
    print("\nActual Grades:")
    print(y_test.values)

    print("\nPredicted Grades:")
    print(y_pred)

    print("\nActual vs Predicted:")
    result = pd.DataFrame({
        "Actual_Grade": y_test.values,
        "Predicted_Grade": y_pred
    })
    print(result)

    # Predict grade for new student
    new_student = pd.DataFrame(
        [[6, 82]],
        columns=["Study_Hours", "Attendance"]
    )

    predicted_grade = model.predict(new_student)
    print("\nPredicted Grade for New Student:", predicted_grade[0])


# ============================================================
# PRACTICAL 5: MULTICLASS CLASSIFICATION USING SOFTMAX
# ============================================================

def practical_5():
    # Create the student dataset
    df = create_student_data()

    # Save and load stud.csv, as used in the PDF
    df.to_csv("stud.csv", index=False)
    print("stud.csv created successfully.")

    df = pd.read_csv("stud.csv")

    # Display dataset
    print("\nStudent Dataset:")
    print(df.head())

    # Independent and dependent variables
    X = df[["Study_Hours", "Attendance"]]
    y = df["Grade"]

    # Split data using stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Logistic Regression uses softmax for multiclass
    # probability estimation with the lbfgs solver
    model = LogisticRegression(
        solver="lbfgs",
        max_iter=1000
    )

    # Train model
    model.fit(X_train, y_train)

    # Predict test data
    y_pred = model.predict(X_test)

    # Display actual and predicted grades
    print("\nActual Grades:")
    print(y_test.values)

    print("\nPredicted Grades:")
    print(y_pred)

    print("\nActual vs Predicted:")
    result = pd.DataFrame({
        "Actual_Grade": y_test.values,
        "Predicted_Grade": y_pred
    })
    print(result)

    # Predict grade for a new student
    new_student = pd.DataFrame(
        [[6, 82]],
        columns=["Study_Hours", "Attendance"]
    )

    predicted_grade = model.predict(new_student)
    print("\nPredicted Grade:", predicted_grade[0])


# ============================================================
# MAIN MENU: SELECT ANY PRACTICAL
# ============================================================

practicals = {
    1: practical_1,
    2: practical_2,
    3: practical_3,
    4: practical_4,
    5: practical_5
}

while True:
    print("\n==========================================")
    print(" FUNDAMENTALS OF MACHINE LEARNING")
    print(" PRACTICAL MENU")
    print("==========================================")
    print("1. Employee CSV and EDA")
    print("2. House Price Prediction - Linear Regression")
    print("3. Spam Classification - Logistic Regression")
    print("4. Student Grades - One-vs-Rest Classification")
    print("5. Student Grades - Softmax Classification")
    print("0. Exit")

    try:
        choice = int(input("Enter practical number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 0:
        print("Program ended.")
        break

    if choice in practicals:
        print("\n--- PRACTICAL", choice, "---")
        try:
            practicals[choice]()
        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)
    else:
        print("Invalid choice. Select 0 to 5.")
