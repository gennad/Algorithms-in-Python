class Tree:
    """
    Binary tree.

    >>> t = Tree(Tree("a", "b"), Tree("c", "d"))
    >>> t.right.left
    'c'
    """

    [1, 1, 2, 6, 24, 120]
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Tree:
    """
    Multiway tree class.

    >>> t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
    >>> t.kids.next.next.val
    'c'
    """
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next

class Bunch(dict):
    """
    The Bunch pattern.

    >>> x = Bunch(name="Jayne Cobb", position="Public Relations")
    >>> x.name
    'Jayne Cobb'
    Second, by subclassing dict, you get lots of functionality for free, such as iterating over the keys/attributes
    or easily checking whether an attribute is present. Here’s an example:
    >>> T = Bunch
    >>> t = T(left=T(left="a", right="b"), right=T(left="c"))
    >>> t.left
    {'right': 'b', 'left': 'a'}
    >>> t.left.right
    'b'
    >>> t['left']['right']
    'b'
    >>> "left" in t.right
    True
    >>> "right" in t.right
    False
    """
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self


if __name__ == "__main__":
    import doctest
    doctest.testmod()
