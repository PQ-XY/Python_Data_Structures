"""
File: arraylistiterator.py
Project 9.3

ArrayListIterator, which allows replacements and insertions, is a subclass
of ArraySortedListIterator.

ArraySortedListIterator supports navigation and removals only.
"""

class ArraySortedListIterator(object):
    """Represents the list iterator for an array-based sorted list."""

    def __init__(self, backingStore):
        self.backingStore = backingStore
        self.modCount = backingStore.getModCount()
        self.first()

    def first(self):
        """Returns the cursor to the beginning of the backing store."""
        self.cursor = 0
        self.lastItemPos = -1

    def hasNext(self):
        """Returns True if the iterator has a next item or False otherwise."""
        return self.cursor < len(self.backingStore)

    def next(self):
        """Preconditions: hasNext returns True
        The list has not been modified except by this iterator's mutators.
        Returns the current item and advances the cursor to the next item.
        Postcondition: lastItemPos is now defined.
        Raises: ValueError if no next item.
        AttributeError if illegal mutation of backing store."""
        # Write you code here

    def last(self):
        """Moves the cursor to the end of the backing store."""
        self.cursor = len(self.backingStore)
        self.lastItemPos = -1

    def hasPrevious(self):
        """Returns True if the iterator has a previous item or False otherwise."""
        return self.cursor > 0

    def previous(self):
        """Preconditions: hasPrevious returns True
        The list has not been modified except by this iterator's mutators.
        Returns the current item and moves the cursor to the previous item.
        Postcondition: lastItemPos is now defined.
        Raises: ValueError if no next item.
        AttributeError if illegal mutation of backing store."""
        # Write your code here

    def remove(self):                
        """Preconditions: the current position is defined.
        The list has not been modified except by this iterator's mutators.
        Pops the item at the current position.
        Raises: AttibuteError if position is not defined.
        AttributeError if illegal mutation of backing store."""
        # Write your code here
        

class ArrayListIterator(ArraySortedListIterator):
    """Represents the list iterator for an array-based list."""

    def __init__(self, backingStore):
        ArraySortedListIterator.__init__(self, backingStore)

    def replace(self, item):
        """Preconditions: the current position is defined.
        The list has not been modified except by this iterator's mutators.
        Replaces the items at the current position with item.
        Raises: AttibuteError if position is not defined.
        AttributeError if illegal mutation of backing store."""
        # Write your code here
       
    def insert(self, item):         
        """Preconditions:
        The list has not been modified except by this iterator's mutators.
        Adds item to the end if the current position is undefined, or
        inserts it at that position.
        Raises: AttributeError if illegal mutation of backing store."""
        # Write your code here
        
