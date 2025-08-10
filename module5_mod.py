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