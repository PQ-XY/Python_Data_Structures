"""
File: hashset.py

Adjusts the array's capacity and rehashes if the load factor > .8 after creating
the HashSet.
"""
"""
Yao Xu
07/12/2025

In this program, I implemented two methods: loadFactor() and rehash(). I also updated the __init__ method, clear(), add(), 
remove() methods to complete the logic of updating the new instance variable "occupiedCells". 

In loadFactor() method, we simply return the result of occupied cells divided by the capacity of the array. 

In rehash() method, I save the set’s items in a list, set the set’s size and number of occupied items to 0, double the 
size of the array, and add the items from the list to the set.

"""

from node import Node
from arrays import Array
from abstractcollection import AbstractCollection
from abstractset import AbstractSet

class HashSet(AbstractSet, AbstractCollection):
    """Represents a hash-based set."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection = None,
                 capacity = None):
        """added a new instance called occupiedCells to keep track of occupied cells."""
        self.occupiedCells = 0
        self.size = 0
        if capacity is None:
            self.capacity = HashSet.DEFAULT_CAPACITY
        else:
            self.capacity = capacity
        self.array = Array(self.capacity)
        self.foundNode = self.priorNode = None
        self.index = -1
        AbstractCollection.__init__(self, sourceCollection)
        """added the logic for rehash(). We repeatedly run the rehash method until the load factor drops below 0.8"""
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
            while self.loadFactor() > 0.8:
                self.rehash()

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self or False otherwise."""
        self.index = abs(hash(item)) % len(self.array)
        self.priorNode = None
        self.foundNode = self.array[self.index]
        while self.foundNode != None:
            if self.foundNode.data == item: 
                return True
            else:
                self.priorNode = self.foundNode
                self.foundNode = self.foundNode.next
        return False
    
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        for node in self.array:
            while node != None:
                yield node.data
                node = node.next

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        """updated the occupied cells of the hashset."""
        self.occupiedCells = 0
        self.foundNode = self.priorNode = None
        self.index = -1
        self.array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        if not item in self:
            if self.array[self.index] == None:
                """updated the occupied cells of the hashset."""
                self.occupiedCells += 1
            self.array[self.index] = Node(item, self.array[self.index])
            self.size += 1
            
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if not item in self:
            raise KeyError(str(item) + " not in set")
        elif self.priorNode == None:
            self.array[self.index] = self.foundNode.next
            """updated the occupied cells of the hashset."""
            self.occupiedCells -= 1
        else:
            self.priorNode.next = self.foundNode.next
        self.size -= 1

    def loadFactor(self):
        """
        return the result of occupied cells divided by the capacity of the array
        """
        return self.occupiedCells / self.capacity

    def rehash(self):
        """
        save the set’s items in a list, set the set’s size and number of occupied items to 0, double the
        size of the array, and add the items from the list to the set
        """
        temp_list = list(self)
        self.capacity *= 2
        self.array = Array(self.capacity)
        self.size = 0
        self.occupiedCells = 0
        self.foundNode = self.priorNode = None
        self.index = -1

        for item in temp_list:
            self.add(item)


if __name__ == "__main__":

    """
    Driver program to test the methods. I added enough items to push the load factor above 0.8 to trigger rehash(). And 
    tested add() and remove() to check the updates on the instances.
    """

    set1 = HashSet([1, 5, 7, 9, 13, 17, 19, 21, 23, 26, 29, 31, 33, 34, 35])
    print(f'Current set: {set1}')
    print(f'Current capacity: {set1.capacity}')
    print(f'Current size: {set1.size}')
    print(f'Current occupied cells: {set1.occupiedCells}')
    print(f'Current load factor: {set1.loadFactor()}')
    print(f'7 is in the set: {7 in set1}')
    print(f'9 is in the set: {9 in set1}')

    set1.add(15)
    set1.add(38)
    print(f'\nCurrent set: {set1}')
    print(f'Current capacity: {set1.capacity}')
    print(f'Current size: {set1.size}')
    print(f'Current occupied cells: {set1.occupiedCells}')
    print(f'Current load factor: {set1.loadFactor()}')

    set1.remove(17)
    set1.remove(9)
    print(f'\nCurrent set: {set1}')
    print(f'Current capacity: {set1.capacity}')
    print(f'Current size: {set1.size}')
    print(f'Current occupied cells: {set1.occupiedCells}')
    print(f'Current load factor: {set1.loadFactor()}')