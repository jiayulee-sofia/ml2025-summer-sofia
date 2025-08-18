import sys
import numpy as np


class KNNRegressor1D:
    """Simple k-NN regressor for 1D inputs using NumPy."""

    def __init__(self):
        self.xs = []
        self.ys = []

    def add_point(self, x: float, y: float) -> None:
        self.xs.append(float(x))
        self.ys.append(float(y))

    def _to_numpy(self):
        if len(self.xs) == 0:
            return np.array([]), np.array([])
        return np.asarray(self.xs, dtype=float), np.asarray(self.ys, dtype=float)

    def predict(self, x_query: float, k: int) -> float:
        X, Y = self._to_numpy()
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        if k > len(X):
            raise ValueError("k must be less than or equal to the number of points (N).")

        # Compute absolute distances in 1D
        dists = np.abs(X - float(x_query))

        # Indices of k nearest neighbors
        nn_idx = np.argsort(dists)[:k]

        # Simple k-NN regression
        return float(np.mean(Y[nn_idx]))


def read_int(prompt: str) -> int:
    while True:
        s = input(prompt)
        try:
            val = int(s)
            return val
        except ValueError:
            print("Please enter an integer.")


def read_pos_int(prompt: str) -> int:
    while True:
        v = read_int(prompt)
        if v > 0:
            return v
        print("Please enter a positive integer.")


def read_float(prompt: str) -> float:
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print("Please enter a real number (e.g., 3, -2.5, 0.001).")


def main():
    # Read N and k
    N = read_pos_int("Enter a positive integer N: ")
    k = read_pos_int("Enter a positive integer k: ")

    reg = KNNRegressor1D()

    # Read N (x, y) points
    for i in range(1, N + 1):
        x_i = read_float(f"Enter x for point {i}: ")
        y_i = read_float(f"Enter y for point {i}: ")
        reg.add_point(x_i, y_i)

    # Read query X
    X_query = read_float("Enter a query X (real number): ")

    # Predict or print error if k > N
    try:
        y_pred = reg.predict(X_query, k)
        print(y_pred)
    except ValueError as e:
        # Any error message acceptable
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
