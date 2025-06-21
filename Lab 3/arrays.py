
class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.logicalSize = 0
        self.defaultCapacity = capacity
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        self.items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self.logicalSize

    def grow(self):
        temp = Array(len(self.items) * 2)
        for i in range(self.logicalSize):
            temp.items[i] = self.items[i]
        self.items = temp.items

    def shrink(self):
        new_capacity = max(self.defaultCapacity, len(self.items) // 2)
        if new_capacity < len(self.items):
            temp = Array(new_capacity)
            for i in range(self.logicalSize):
                temp.items[i] = self.items[i]
            self.items = temp.items


def main():
    """Test code for modified Array class."""
    a = Array(5)
    print("Physical size:", len(a))
    print("Logical size:", a.size())
    print("Items:", a)
    a.grow()
    print("Items:", a)
    a.grow()
    print("Items:", a)
    a.shrink()
    print("Items:", a)
    a.shrink()
    print("Items:", a)
    a.shrink()
    print("Items:", a)

if __name__ == "__main__":
    main()
