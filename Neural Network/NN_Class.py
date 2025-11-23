import numpy as np

class NeuralNetwork:
    def _init_(self, X, Y, layers_dim, learning_rate=0.01):
        self.X = X
        self.Y = Y
        self.layers_dim = layers_dim
        self.learning_rate = learning_rate
        self.parameters = self.initialize_parameters()

    def initialize_parameters(self):
        np.random.seed(1)
        parameters = {}
        for l in range(1, len(self.layers_dim)):
            parameters[f"W{l}"] = np.random.randn(self.layers_dim[l], self.layers_dim[l-1] + 1) * 0.01
        return parameters

    def _sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))

    def _sigmoid_derivative(self, A):
        return A * (1 - A)

    def _tanh_derivative(self, A):
        return 1 - np.power(A, 2)

    def forward_propagation(self):
        A = self.X
        caches = []
        L = len(self.parameters)

        for l in range(1, L):
            A_with_bias = np.vstack((np.ones((1, A.shape[1])), A))   # add bias
            Z = np.dot(self.parameters[f"W{l}"], A_with_bias)
            A = np.tanh(Z)
            caches.append((A, Z, self.parameters[f"W{l}"], A_with_bias))

        # Output layer with sigmoid
        A_with_bias = np.vstack((np.ones((1, A.shape[1])), A))
        ZL = np.dot(self.parameters[f"W{L}"], A_with_bias)
        AL = self._sigmoid(ZL)
        caches.append((AL, ZL, self.parameters[f"W{L}"], A_with_bias))

        return AL, caches

    def compute_cost(self, AL):
        m = self.Y.shape[1]
        cost = (-1/m) * np.sum(self.Y * np.log(AL + 1e-8) + (1 - self.Y) * np.log(1 - AL + 1e-8))
        return np.squeeze(cost)

    def backward_propagation(self, AL, caches):
        grads = {}
        m = self.X.shape[1]
        L = len(caches)

        # Output layer
        dZ = AL - self.Y
        A_prev_with_bias = caches[L-1][3]
        grads[f"dW{L}"] = (1/m) * np.dot(dZ, A_prev_with_bias.T)

        # Hidden layers
        for l in reversed(range(1, L)):
            A_curr, Z_curr, W_curr, A_prev_with_bias = caches[l-1]
            if l == L-1:
                W_next = self.parameters[f"W{l+1}"]
                dZ_next = AL - self.Y
                W_no_bias = W_next[:, 1:]
                dA = np.dot(W_no_bias.T, dZ_next)
            else:
                W_next = self.parameters[f"W{l+1}"]
                dZ_next = dZ
                W_no_bias = W_next[:, 1:]
                dA = np.dot(W_no_bias.T, dZ_next)

            dZ = dA * self._tanh_derivative(A_curr)
            grads[f"dW{l}"] = (1/m) * np.dot(dZ, A_prev_with_bias.T)

        return grads

    def update_parameters(self, grads):
        L = len(self.parameters)
        for l in range(1, L+1):
            self.parameters[f"W{l}"] -= self.learning_rate * grads[f"dW{l}"]

    def train(self, num_iterations=1000, print_cost=False):
        for i in range(num_iterations):
            AL, caches = self.forward_propagation()
            cost = self.compute_cost(AL)
            grads = self.backward_propagation(AL, caches)
            self.update_parameters(grads)
            if print_cost and i % 500 == 0:
                print(f"Iteration {i}: cost = {cost:.4f}")

    def predict(self, X):
        A = X
        L = len(self.parameters)
        for l in range(1, L):
            A_with_bias = np.vstack((np.ones((1, A.shape[1])), A))
            Z = np.dot(self.parameters[f"W{l}"], A_with_bias)
            A = np.tanh(Z)
        A_with_bias = np.vstack((np.ones((1, A.shape[1])), A))
        ZL = np.dot(self.parameters[f"W{L}"], A_with_bias)
        AL = self._sigmoid(ZL)
        return (AL > 0.5).astype(int)
