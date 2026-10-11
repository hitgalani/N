# Complete explanation of your ML practical code

Your program contains two main practicals from your Fundamentals of Machine Learning course:

1. Q1: Exploratory Data Analysis (EDA) — understanding and analyzing employee data.
2. Q2: Simple Linear Regression — predicting house prices from house size.

I will explain the functions, their purpose, what they return, and why they are used in your code.

## Part 1: Importing libraries

```
import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as snsfrom sklearn.model_selection import train_test_splitfrom sklearn.linear_model import LinearRegressionfrom sklearn.metrics import r2_score, mean_squared_error
```

| Library/function            | Purpose                                                       |
| --------------------------- | ------------------------------------------------------------- |
| `pandas` (`pd`)             | Creates and manages tables using DataFrames.                  |
| `numpy` (`np`)              | Performs numerical calculations, including square roots.      |
| `matplotlib.pyplot` (`plt`) | Creates graphs such as histograms and scatter plots.          |
| `seaborn` (`sns`)           | Creates statistical visualizations such as heatmaps.          |
| `train_test_split()`        | Divides data into training and testing sets.                  |
| `LinearRegression()`        | Creates a simple linear regression model.                     |
| `r2_score()`                | Measures how well the model explains variation in the target. |
| `mean_squared_error()`      | Calculates average squared prediction error.                  |

# Part 2: Q1 — Exploratory Data Analysis (EDA)

## 1. Creating the employee dataset

```
employees = {    "Emp_ID": list(range(101, 121)),    "Name": [...],    "Department": [...],    "Salary": [...],    "Experience": [...]}df = pd.DataFrame(employees)
```

- `employees` is a Python dictionary containing five columns.
- `range(101, 121)` generates employee IDs from 101 to 120.
- `list()` converts the range into a list.
- `pd.DataFrame()` converts the dictionary into a tabular dataset.
- `df` is the variable holding that table.

Your dataset contains 20 employees, with salary and experience as numerical columns.

You create `df` twice in your current code. The second `df = pd.DataFrame(employees)` is redundant; you can remove it.

## 2. Displaying the dataset

```
print(df)
```

Displays all 20 employee records.

```
print(df.head())
```

`head()` displays the first five rows by default. To display ten rows, use `df.head(10)`.

```
print(df.info())
```

`info()` displays information such as column names, non-null counts, data types and memory usage.

Important: `df.info()` prints its information directly and returns `None`. Therefore, you can simply write:

```
df.info()
```

This avoids printing an extra `None` at the end.

```
print(df.shape)
```

Returns a tuple in the form `(rows, columns)`.

For your dataset, the result is `(20, 5)`.

```
print(df.describe())
```

Provides descriptive statistics for numerical columns, including:

- `count`: number of non-missing values.
- `mean`: arithmetic average.
- `std`: standard deviation.
- `min`: minimum.
- `25%`, `50%`, `75%`: quartiles.
- `max`: maximum.

## 3. Checking missing data

```
print(df.isnull().sum())
```

These functions work together:

- `isnull()` identifies missing values and returns `True` or `False`.
- `sum()` counts the `True` values in each column.

For example, if two salary entries were missing, the Salary result would be `2`.

Your supplied employee dataset has no missing values, so filling missing data is unnecessary for this particular run.

## 4. Calculating salary statistics

```
print("Mean:", df["Salary"].mean())print("Median:", df["Salary"].median())print("Mode:", df["Salary"].mode().tolist())print("Variance:", df["Salary"].var())print("Standard Deviation:", df["Salary"].std())
```

`df["Salary"]`

Selects the Salary column as a Pandas Series.

`.mean()`

Calculates the arithmetic average:

\\[ \text{Mean}=\frac{\sum x_i}{n} \\]

`.median()`

Returns the middle value after sorting the salaries. For an even number of observations, it averages the two middle values.

`.mode()`

Returns the most frequently occurring value or values. If every salary occurs only once, all salaries are modes.

`.var()`

Calculates sample variance by default, measuring squared deviations from the mean.

`.std()`

Calculates sample standard deviation, which expresses the spread in the same units as salary.

The `tolist()` method converts the mode result from a Pandas Series into an ordinary Python list.

## 5. Drawing the salary histogram

```
plt.hist(df["Salary"], bins=6, edgecolor="black")plt.xlabel("Salary")plt.ylabel("Frequency")plt.title("Univariate Analysis: Salary Distribution")plt.show()
```

- `plt.hist()` creates a histogram.
- `bins=6` divides the salary range into six intervals.
- `edgecolor="black"` adds borders to the bars.
- `xlabel()` labels the horizontal axis.
- `ylabel()` labels the vertical axis.
- `title()` adds the graph title.
- `show()` displays the graph.

A histogram is univariate analysis because it examines one variable: Salary.

## 6. Drawing the Experience vs Salary scatter plot

```
plt.scatter(df["Experience"], df["Salary"])plt.xlabel("Experience (Years)")plt.ylabel("Salary")plt.title("Experience vs Salary")plt.show()
```

`plt.scatter(x, y)` draws individual data points to show the relationship between two numerical variables.

- X-axis: employee experience.
- Y-axis: employee salary.
- Each point represents one employee.

This is bivariate analysis because it studies two variables.

If the points generally move upward from left to right, it suggests a positive relationship: employees with more experience tend to have higher salaries. A scatter plot shows association, not necessarily causation.

## 7. Selecting numerical columns

```
numeric_df = df.select_dtypes(include=np.number)
```

`select_dtypes()` selects columns according to their data types.

- `include=np.number` selects numerical columns.
- In your dataset, the selected columns are `Emp_ID`, `Salary` and `Experience`.
- Text columns such as `Name` and `Department` are excluded.

Although `Emp_ID` is stored as a number, it is an identifier, not a meaningful measurement. For substantive correlation analysis, you should generally exclude it.

## 8. Calculating the correlation matrix

```
correlation_matrix = numeric_df.corr()print("\n--- Correlation Matrix ---")print(correlation_matrix)
```

`.corr()` calculates pairwise Pearson correlation coefficients by default.

The correlation coefficient ranges from \\(-1\\) to \\(+1\\):

| Value     | Interpretation                      |
| --------- | ----------------------------------- |
| Near `+1` | Strong positive linear relationship |
| Near `-1` | Strong negative linear relationship |
| Near `0`  | Little or no linear relationship    |

Correlation measures the strength and direction of a linear relationship. It does not prove that one variable causes another.

## 9. Creating the correlation heatmap

```
sns.heatmap(    correlation_matrix,    annot=True,    cmap="coolwarm",    fmt=".2f")plt.title("Employee Numerical Correlation Heatmap")plt.show()
```

- `sns.heatmap()` visualizes the correlation matrix.
- `annot=True` displays each coefficient inside its cell.
- `cmap="coolwarm"` uses a contrasting color scheme.
- `fmt=".2f"` formats the values to two decimal places.
- `plt.title()` sets the heading.
- `plt.show()` displays the chart.

This is multivariate analysis because it examines relationships among multiple numerical variables simultaneously.

# Part 3: Q2 — Simple Linear Regression

## 10. Creating the house dataset

```
data = {    "House_Size": [...],    "Price": [...]}house_df = pd.DataFrame(data)print(house_df)
```

- `House_Size` contains the house areas in square feet.
- `Price` contains the corresponding prices in the dataset's units.
- `pd.DataFrame(data)` creates the house dataset.
- `print(house_df)` displays all 15 records.

The price values do not specify a currency or scale, so your output should retain the label `Price (Dataset Units)` unless your assignment provides a unit.

## 11. Defining independent and dependent variables

```
X = house_df[["House_Size"]]y = house_df["Price"]print("\nIndependent", X.columns.tolist())print("Dependent", y.name)
```

`X` — independent variable

- `house_df[["House_Size"]]` selects the input feature.
- Double brackets produce a DataFrame, which scikit-learn expects for its input features.
- `X.columns.tolist()` returns the column names as a list.

`y` — dependent variable

- `house_df["Price"]` selects the target column.
- Single brackets produce a Series.
- `y.name` returns the target's name, `Price`.

The model learns to predict Price from House_Size.

## 12. Splitting training and testing data

```
X_train, X_test, y_train, y_test = train_test_split(    X,    y,    test_size=0.20,    random_state=42)
```

`train_test_split()` divides the dataset into two parts.

| Parameter or variable | Meaning                             |
| --------------------- | ----------------------------------- |
| `X`                   | Input features                      |
| `y`                   | Target values                       |
| `test_size=0.20`      | 20% of observations for testing     |
| `random_state=42`     | Makes the random split reproducible |
| `X_train`             | Training input features             |
| `X_test`              | Testing input features              |
| `y_train`             | Training target values              |
| `y_test`              | Actual target values for testing    |

With 15 records, this produces 12 training records and 3 testing records.

The model learns from the training data. The testing data evaluates how well it predicts observations not used during fitting.

## 13. Creating and training the model

```
model = LinearRegression()model.fit(X_train, y_train)
```

- `LinearRegression()` creates the linear regression estimator.
- `model` stores the estimator.
- `.fit()` trains the model using the training inputs and known prices.

Simple linear regression fits a line in the form:

\\[ \hat{y}=mx+b \\]

Where:

- \\(\hat{y}\\) = predicted price.
- \\(x\\) = house size.
- \\(m\\) = slope.
- \\(b\\) = intercept.

The model estimates the slope and intercept using ordinary least squares, minimizing the sum of squared residuals on the training data.

## 14. Displaying slope and intercept

```
print("Slope:", model.coef_[0])print("Intercept:", model.intercept_)
```

- `model.coef_` stores the fitted coefficient for each input feature.
- `[0]` selects the coefficient for the first feature, House_Size.
- `model.intercept_` returns the fitted intercept.

The slope indicates the model's predicted change in price for each additional square foot. The intercept is the fitted price at zero square feet, although that may not be practically meaningful.

## 15. Displaying the regression equation

```
print(    f"Equation: Price = {model.coef_[0]:.4f}"    f" * House_Size + {model.intercept_:.4f}")
```

- `f"..."` is an f-string that inserts values into text.
- `{model.coef_[0]:.4f}` displays the slope to four decimal places.
- `{model.intercept_:.4f}` displays the intercept to four decimal places.
- Adjacent f-strings are joined automatically.

The output expresses the fitted model as:

`Price = slope × House_Size + intercept`

The exact slope and intercept depend on the fitted training data.

## 16. Predicting prices for the test set

```
y_pred = model.predict(X_test)
```

`.predict()` uses the trained model to estimate prices for the test-set house sizes.

- `X_test` contains the test-set house sizes.
- `y_pred` contains the predicted prices.
- These predictions can be compared with `y_test`, the actual prices.

## 17. Comparing actual and predicted prices

Your code:

```
results = pd.DataFrame({    "House_Size": X_test["House_Size"].values,    "Actual_Price": y_test.values,    "Predicted_Price": np.round(y_pred, 2)})print(results.to_string(index=False))
```

Explanation:

- `pd.DataFrame({...})` creates a results table.
- `.values` extracts the underlying values from the Series or column.
- `np.round(y_pred, 2)` rounds predictions to two decimal places.
- `.to_string(index=False)` prints the table without row-index numbers.

This table lets you compare the model's estimates against the real test-set prices.

## 18. Evaluating the model

```
r2 = r2_score(y_test, y_pred)print("R2 Score:", r2)mse = mean_squared_error(y_test, y_pred)print("MSE:", mse)rmse = np.sqrt(mse)print("RMSE:", rmse)
```

`r2_score(y_test, y_pred)`

Calculates the coefficient of determination, \\(R^2\\). It compares prediction error against the variation in actual target values. A score closer to 1 generally indicates a better fit; a negative test score is possible.

`mean_squared_error(y_test, y_pred)`

Calculates the mean squared error:

\\[ \operatorname{MSE}=\frac{1}{n}\sum\_{i=1}^{n}(y_i-\hat y_i)^2 \\]

Smaller values generally indicate lower prediction error. Squaring errors penalizes large mistakes more heavily.

`np.sqrt(mse)`

Calculates the root mean squared error (RMSE). It expresses error in the same units as the target price, making it easier to interpret than MSE.

You are calculating these metrics on the test set, which is appropriate for assessing performance on held-out observations.

## 19. Plotting actual data and the regression line

Your current code:

```
plt.scatter(X, y, label="Actual Data")plt.plot(X, model.predict(X), color="red", label="Regression Line")plt.xlabel("House Size (Square Feet)")plt.ylabel("Price (Dataset Units)")plt.title("House Size vs House Price")plt.legend()plt.show()
```

Explanation:

- `plt.scatter(X, y, ...)` plots the observed house sizes and prices.
- `plt.plot(X, model.predict(X), ...)` draws predictions from the fitted model.
- `xlabel()` and `ylabel()` identify the axes.
- `title()` adds the graph heading.
- `legend()` displays the data and line labels.
- `show()` displays the completed plot.

One improvement: Sort the house sizes before plotting the regression line. Your dataset is already sorted, so your current code works for this specific dataset. Sorting makes the code reliable if the rows are later rearranged.

```
plot_df = house_df.sort_values("House_Size")plt.scatter(    house_df["House_Size"],    house_df["Price"],    label="Actual Data")plt.plot(    plot_df["House_Size"],    model.predict(plot_df[["House_Size"]]),    color="red",    label="Regression Line")plt.xlabel("House Size (Square Feet)")plt.ylabel("Price (Dataset Units)")plt.title("House Size vs House Price")plt.legend()plt.show()
```

Notice that `model.predict()` receives the same feature name, `House_Size`, that was used during training.

## 20. Predicting the price of a new house

```
new_house = pd.DataFrame({"House_Size": [1800]})new_price = model.predict(new_house)print("\nPredicted price for a 1800 sq. ft. house:")print(round(new_price[0], 2))
```

- `pd.DataFrame({"House_Size": [1800]})` creates a one-row DataFrame for a new house.
- `model.predict(new_house)` estimates its price using the trained model.
- `new_price[0]` extracts the first prediction.
- `round(new_price[0], 2)` displays the estimate to two decimal places.

Important: This prediction uses the model trained on only the training split. Since 1,800 square feet is within the dataset's observed range, it is an interpolation rather than an extrapolation. The predicted value may differ from the supplied price of 125 because the fitted model does not necessarily pass through every data point.

## 21. Small corrections to your original code

Make these changes for cleaner execution:

1. Remove the duplicate `df = pd.DataFrame(employees)` line.
2. Use `df.info()` instead of `print(df.info())`.
3. Exclude `Emp_ID` from the correlation matrix if you want correlations among meaningful numerical measurements only.
4. Add `plt.legend()` to your employee scatter plot if you provide a label.
5. Sort the house sizes before plotting the regression line.
6. Print the final new-house prediction and completion message.

For the last step, append:

```
print("\nPredicted price for a 1800 sq. ft. house:")print(round(new_price[0], 2))print("\nQ2 completed successfully.")
```

Your two practicals cover core EDA and Simple Linear Regression concepts in your syllabus. The rest of Units 1–4 also includes topics such as automated EDA, classification, logistic regression, loss functions, regularization and cross-validation; those are separate practicals rather than missing functions in this particular program.