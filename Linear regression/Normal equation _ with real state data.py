#this for normal equ. single variable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv("data.csv", names=["population", "profit"])

# Add ones column for the intercept
data.insert(0, 'Ones', 1)

# Separate features (X) and target (y)
cols = data.shape[1]
X = data.iloc[:, 0:cols-1]  # Features
y = data.iloc[:, cols-1:cols]  # Target variable

# Convert to numpy matrices
X = np.matrix(X.values)
y = np.matrix(y.values)

# Compute theta using Normal Equation
theta = np.linalg.inv(X.T @ X) @ X.T @ y

print("Theta computed from Normal Equation:\n", theta)

# Plot best-fit line
x = np.linspace(data.population.min(), data.population.max(), 100)
f = theta[0, 0] + (theta[1, 0] * x)

fig, ax = plt.subplots(figsize=(5,5))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.population, data.profit, label='Training Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Linear Regression using Normal Equation')
plt.show()
