import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def read_int(prompt: str) -> int:
    while True:
        s = input(prompt)
        try:
            return int(s)
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
    N = read_pos_int("Enter a positive integer N: ")
    k = read_pos_int("Enter a positive integer k: ")

    Xs = np.empty(N, dtype=float)
    Ys = np.empty(N, dtype=float)

    for i in range(N):
        xi = read_float(f"Enter x for point {i+1}: ")
        yi = read_float(f"Enter y for point {i+1}: ")
        Xs[i] = xi
        Ys[i] = yi

    y_variance = np.var(Ys, ddof=0)
    print(f"Variance of labels (Y) in training data: {y_variance}")

    X_query = read_float("Enter a query X (real number): ")

    if k > N:
        print("Error: k must be less than or equal to N.")
        return

    X_mat = Xs.reshape(-1, 1)
    knn = KNeighborsRegressor(n_neighbors=k, weights="uniform", metric="minkowski", p=2)
    knn.fit(X_mat, Ys)

    y_pred = knn.predict(np.array([[X_query]], dtype=float))[0]
    print(f"k-NN Regression prediction for X={X_query}: {y_pred}")


if __name__ == "__main__":
    main()