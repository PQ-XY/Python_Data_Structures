"""
File: linkedbst.py
Adds a method to rebalance the tree.
"""
"""
Yao Xu
7/11/2025

In this program, I implemented two methods--rebalance() and isBalanced(). 

In the rebalance() method, I first collect all the elements of the tree in the sorted order by using the inorder traversal.
Then I clear the existing tree and rebuild it by recursively inserting the middle element of each list segment.

In the isBalanced() method, it is not strict. For example, 
                             1
                            |  |
                           2   3
                           |
                          4
                         | 
                        5
this tree height is 3. 2 *log(len(self) + 1, 2) - 1 = 4.17. 3 < 4.17, so the method return True. But this is not balanced.
The definition states that for every node, the heights of its left and right subtrees differ by at most 1. In the example
above, the left subtree and right subtree of the root is 2. 
In order to make this method a strict check, we need go with the definition. We need to check every node in the tree that 
the heights of its left and right subtrees differ by at most 1 recursively. In my implementation, I used preorder. 
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from math import log
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue

class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.root = None
        AbstractCollection.__init__(self, sourceCollection)
        
    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self.root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self.root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                lyst.append(node.data)
                recurse(node.left)
                recurse(node.right)
        recurse(self.root)
        return iter(lyst)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self.root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self.root)
        return iter(lyst)

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        lyst = list()
        queue = LinkedQueue()
        if not self.isEmpty():
            queue.add(self.root)
        while not queue.isEmpty():
            node = queue.pop()
            lyst.append(node.data)
            if node.left != None:
                queue.add(node.left)
            if node.right != None:
                queue.add(node.right)
        return iter(lyst)

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        def recurse(node):
            if node is None:
                return None
            elif node.data == item:
                return node.data
            elif node.data > item:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self.root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.root = None
        self.size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position 
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal, 
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self.root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self.root)
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty(): return None
        
        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self.root
        parent = preRoot
        direction = 'L'
        currentNode = self.root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right
                
        # Return None if the item is absent
        if itemRemoved == None: return None
        
        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
           and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
            
        # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right
                
        # Case 3: The node has no right child
            else:
                newChild = currentNode.left
                
        # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild
            
        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self.size -= 1
        if self.isEmpty():
            self.root = None
        else:
            self.root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self.root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        """Returns the height of the tree (the length of the longest path
        from the root to a leaf node).
        When len(t) < 2, t.height() == 0."""
        def recurse(node):
            if node == None:
                return 0
            else:
                return 1 + max(recurse(node.left), recurse(node.right))
        h = recurse(self.root)
        if not self.isEmpty():
            h -= 1
        return h

    def rebalance(self):
        """
        Rebalances the tree so that it becomes height-balanced, with minimal height for the current set of elements.
        """
        val_list = list(self.inorder())
        self.clear()

        def build_tree(vals):
            """base case"""
            if len(vals) == 0:
                return
            mid = len(vals) // 2
            self.add(vals[mid])
            build_tree(vals[:mid])
            build_tree(vals[mid + 1:])

        build_tree(val_list)

    def isBalanced(self):
        """
        Returns True if the tree is balanced or False otherwise.
        We are using a helper function to determine if a tree is balanced for every node of the tree recursively.
        """
        def recurse(node):
            """base case"""
            if node == None:
                return 0, True
            left_height, left_is_balanced = recurse(node.left)
            right_height, right_is_balanced = recurse(node.right)
            balanced = (left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1)
            return max(left_height, right_height) + 1, balanced
        height, is_balanced = recurse(self.root)
        return is_balanced

if __name__ == "__main__":
    """
    This is a driver program for testing the isBalanced() function and rebalance() function.
    """

    tree = LinkedBST()

    """create an imbalanced tree"""
    for i in range (0, 10):
        tree.add(i)

    print(f'Current tree: \n{tree}')
    print(f'Is balanced?: {tree.isBalanced()}')
    print(f'Tree height: {tree.height()}')

    tree.rebalance()

    print(f'Current tree: \n{tree}')
    print(f'Is balanced?: {tree.isBalanced()}')
    print(f'Tree height: {tree.height()}')


