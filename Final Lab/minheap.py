"""
File: minheap.py

The program implements a MinHeap class.
"""

class MinHeap:

    def __init__(self):
        """Using list as the underlying data structure."""
        self.heap = []

    def isEmpty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return iter(sorted(self.heap))

    def __str__(self):
        return str(self.heap)

    def __contains__(self, item):
        return item in self.heap

    def __add__(self, other):
        new_heap = MinHeap()
        for item in self.heap + other.heap:
            new_heap.add(item)
        return new_heap

    def __eq__(self, other):
        if not isinstance(other, MinHeap):
            return False
        return sorted(self.heap) == sorted(other.heap)

    def peek(self):
        """Returns the topmost item in heap."""
        if self.isEmpty():
            raise IndexError("heap is empty")
        return self.heap[0]

    def add(self, item):
        """Inserts item in its proper place in heap."""
        self.heap.append(item)
        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        """Removes and returns the topmost item in heap."""
        if self.isEmpty():
            raise IndexError("heap is empty")
        self.swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self.bubble_down(0)
        return item

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def bubble_up(self, i):
        """Helper function when adding an element to the heap."""
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self.bubble_up(parent)

    def bubble_down(self, i):
        """Helper function when removing an element to the heap."""
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.bubble_down(smallest)


