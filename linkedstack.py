from node import Node
from abstractstack import AbstractStack


class LinkedStack(AbstractStack):
    """A Link-based stack implementation."""

    def __init__(self, sourceCollection=None):
        self._items = None
        AbstractStack.__init__(self, sourceCollection)

    # Accessors
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        def visitNodes(node):
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList = list()
        visitNodes(self._items)
        return iter(tempList)

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            # raise KeyError("The stack is empty.")
            return None
        return self._items.data

    # Mutator
    def clear(self):
        """Makes the self become empty."""
        self._size = 0
        self._items = None

    def push(self, item):
        """Inserts item at the top of the stack."""
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            # raise KeyError("The stack is empty.")
            print("The stack is empty.")
            return None
        oldItem = self._items.data
        self._items = self._items.next
        self._size -= 1
        return oldItem

    # #This Function is for the game
    # def contains(self, number):
    #     """Checks if the stack contains the number and if so returns the position
    #     otherwise returns None"""
    #     if self.isEmpty():
    #         return False
    #     count = 0
    #     while count < len(self) - 1:
    #         if self._items.data == number:
    #             return True
    #         else:
    #             self._items = self._items.next
    #             count += 1
    #     return False

    def __contains__(self, item):
        for i in self:
            if i == item:
                return True
        return False

    def getIndex(self, item):
        """Pre: the stack DOES contain the item"""
        count = self._size-1
        for i in self:
            if i == item:
                return self._size- count
            count -= 1