"""
File: counter.py
Author: Ken Lambert
"""

class Counter(object):
    """Represents a counter object."""

    def __init__(self):
        self.number = 0

    def increment(self, amount = 1):
        self.number += amount

    def __str__(self):
        return str(self.number)

    def reset(self):
        self.number = 0
