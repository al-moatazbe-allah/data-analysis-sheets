import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("3_groups.csv")
X = df[['x', 'y']].values

# K-Means function
def kmeans(X, k=3, iterations=100):
    np.random.seed(42)
    centroids = X[np.random.choice(len(X), k, replace=False)]

    for _ in range(iterations):
        # Assign clusters
        distances = np.sqrt(((X[:, np.newaxis] - centroids)**2).sum(axis=2))
        labels = np.argmin(distances, axis=1)

        # Update centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, labels

centroids, labels = kmeans(X)

# Plot clusters
plt.scatter(X[:,0], X[:,1], c=labels)
plt.scatter(centroids[:,0], centroids[:,1], c='red', marker='x', s=200)
plt.title("K-Means Clustering")
plt.show()
