import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Choice.csv")

X = df[['age', 'income']].values
y = df['bought'].values.reshape(-1, 1)

# Normalize inputs
X = (X - X.mean(axis=0)) / X.std(axis=0)

# Add bias column
X_b = np.hstack([np.ones((X.shape[0], 1)), X])

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Training
def train(X, y, lr=0.1, epochs=2000):
    m, n = X.shape
    W = np.zeros((n, 1))
    losses = []

    for i in range(epochs):
        z = X @ W
        h = sigmoid(z)
        loss = -(y * np.log(h + 1e-9) + (1-y) * np.log(1-h + 1e-9)).mean()
        gradient = X.T @ (h - y) / m
        W -= lr * gradient
        losses.append(loss)

    return W, losses

W, losses = train(X_b, y)

# Plot loss curve
plt.plot(losses)
plt.title("Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

# Predict
pred = (sigmoid(X_b @ W) > 0.5).astype(int)
accuracy = (pred == y).mean()

print("Model Accuracy:", accuracy)
print("Weights:", W.flatten())
