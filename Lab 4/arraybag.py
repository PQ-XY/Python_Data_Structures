"""
Yao Xu
6/22/2025

In this program I implemented two class methods as __contains__() and clone(). The __contains__() method will check if the
item is in the bag or not. The clone() method will create a copy of the bag on which it is called. I also simplified
the remove() method by using the __contains__() method to check if the to be removed item is in the bag, and get the position
using the position variable self.targetIndex.
"""


"""
File: arraybag.py
Author: Ken Lambert
"""

from arrays import Array
from abstractbag import AbstractBag

class ArrayBag(AbstractBag):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.targetIndex = -1
        AbstractBag.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __contains__(self, item):
        """Returns True if item is in self or False otherwise. It also sets self.targetIndex to the found position or -1
        if not found.
        Input:
            item - the item to check
        Output:
            True if item is in self, False otherwise
        """
        self.targetIndex = 0
        for targetItem in self:
           if targetItem == item:
               return True
           self.targetIndex += 1
        self.targetIndex = -1
        return False
        
        
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.targetIndex = -1
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if len(self) == len(self.items):
            temp = Array(2 * len(self))
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary 
        # (the "in" will call the __contains__ method)
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for index of target item (unneeded after implementing __contains__)
        # self.targetIndex = 0
        # for targetItem in self:
        #    if targetItem == item:
        #        break
        #    self.targetIndex += 1
        
        # Shift items to the left of target up by one position
        for i in range(self.targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        # Decrement logical size
        self.size -= 1
        # Check array memory here and decrease it if necessary
        if len(self) < len(self.items) // 3 and \
           2 * len(self) >= ArrayBag.DEFAULT_CAPACITY:
            temp = Array(len(self.items) // 2)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp

    def clone(self):
        """Returns a copy of self."""
        return ArrayBag(self)

def main():
    """
    This is the main function to test the __contains__(), remove() and clone() methods.
    """
    a = ArrayBag([1, 2, 3, 4, 5, 6, 7, 8])
    print(a)
    a.remove(3)
    print(a)
    a.remove(1)
    print(a)
    b = a.clone()
    print(b)
    print(a == b)
    print(a is b)

if __name__ == "__main__":
    main()
