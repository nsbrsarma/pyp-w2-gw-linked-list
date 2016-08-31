class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next
        #pass

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        # compare only element of list - not comparing pointers
        # Need to check for None here
        if self is None and other is None:
            return True
        
        if self is None or other is None:
            return False
            
        return self.elem == other.elem

    def __repr__(self):
        return self
