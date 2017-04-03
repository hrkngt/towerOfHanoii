""" abstractCollection.py"""


class AbstractCollection(object):
    """An abstract collection implementation."""

    # constructor
    def __init__(self, sourceCollection=None):
        """sets the initial state of self,which includes the contents
		of sourceCollection, if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # accessor methods
    def isEmpty(self):
        """returns True if len(self)==0, or false otherwise"""
        return len(self) == 0

    def __len__(self):
        """returns the number of items in self."""
        return self._size

    def __str__(self):
        """returns the string representation of self."""
        return "[" + ",".join(map(str, self)) + "]"

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """returns True if self equals other,or false otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
                        len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
