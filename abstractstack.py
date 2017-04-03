from abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):
    """An abstract stack implementation."""

    #Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of souceCollection, if it's present."""
        AbstractCollection.__init__(self, sourceCollection)

    #Mutator method
    def add(self, item):
        """Adds item to self."""
        self.push(item)
