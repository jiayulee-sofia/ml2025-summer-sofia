class NumberStore:
    """Stores integers and supports insertion and search by value (1-based index)."""

    def __init__(self):
        self.data = []

    def insert_number(self, value: int) -> None:
        self.data.append(value)

    def find_index(self, x: int) -> int:
        """Return 1-based index of first occurrence of x, or -1 if not found."""
        try:
            return self.data.index(x) + 1
        except ValueError:
            return -1


def read_int(prompt: str) -> int:
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("Please enter an integer.")


def main():
    store = NumberStore()

    N = read_int("Enter a positive integer N: ")
    while N <= 0:
        print("N must be positive.")
        N = read_int("Enter a positive integer N: ")

    for i in range(1, N + 1):
        num = read_int(f"Enter number {i}: ")
        store.insert_number(num)

    X = read_int("Enter a number X to search for: ")
    idx = store.find_index(X)
    print(idx)


if __name__ == "__main__":
    main()