from module5_mod import NumberStore


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