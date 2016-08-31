from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
                
        if not elements:
            return
        
        for elem in elements:
            self.append(elem)
        

    def __str__(self):
        ll_str = ""
        max_index = self.count()
        if max_index == 0:
            return "[]"
        
        it = self.start
        for ind in range(0,max_index):
            ll_str += str(it.elem)+", "
            it = it.next
        
        return "[{}]".format(ll_str[:-2])


    def __len__(self):
        # Iterate through until no pointer is left
        it = self.start
        length = 0
        while it:
            length += 1
            it = it.next

        return length
        

    def __iter__(self):
        return self.start
    
    

    def __getitem__(self, index):
        # Raise error if index is invalid
        if type(index) != int or index < 0 or index > self.__len__():
            raise IndexError()

        # Go to given "index" parameter
        it = self.start
        for counter in range(0, index):
            it = it.next
            
        return it.elem

    def __add__(self, other):
        # First make a copy of LinkedList (must be immutable) and then append
        # each element as Node from other LL
        new_linked_list = self.copy()
        
        it2 = other.start
        while it2:
            new_linked_list.append(it2.elem)
            it2 = it2.next
        
        return new_linked_list
    
    def __iadd__(self, other):
        # This is the mutable case
        it = other.start
        while it:
            self.append(it.elem)
            it = it.next
        
        return self

    def __eq__(self, other):
        # Seems to need to check if these are None
        if self.start is None and other.start is None:
            return True
        
        if self.start is None or other.start is None:
            return False
        
        # If lengths are inequal, no need to go through all elements
        if self.__len__() != other.__len__():
            return False

        # Iterate through each element of each list and compare
        it1 = self.start
        it2 = other.start
        while it1:
            if it1.elem != it2.elem:
                return False
            
            it1 = it1.next
            it2 = it2.next
            
        return True
        
    def __ne__(self, other):
        return not(self.__eq__(other))

    def append(self, elem):
        # Instantiate new Node and change links.  Need to check if it is the
        # first element
        aux = Node(elem)
        if self.__len__() == 0:
            self.start = aux
        else:
            self.end.next = aux
        self.end = aux
        # self.length += 1
        

    def count(self):
        # Should be same as length for this case
        return self.__len__()

    def pop(self, index=None):
        
        # Assign index as last index if none
        max_index = self.__len__() - 1 # length - 1 is final index
        if index is None:
            index = max_index
            
        # Raise error if index is invalid
        if type(index) != int or index < 0 or index > max_index:
            raise IndexError()
            
        # If popping first item, need to reassign start
        if index == 0:
            retval = self.start.elem
            self.start = self.start.next
            return retval
        
        # Otherwise, all cases are similar, but need to treat pop of last
        # item a little differently
        it = self.start

        # Go to index in the list right before the given "index" parameter
        for counter in range(0, index - 1):
            #print(str(counter) + " - " + str(it.elem))
            it = it.next
            
        
        retval = it.next.elem
        
        # Need to change link of item to point to the one after popped item
        # If it is the last item, just need to change self.end
        if index == max_index:
            self.end = it
            self.end.next = None
        else:
            it.next = it.next.next
            
        return retval

    def __copy__(self):
        new_linked_list = LinkedList()
        it = self.start
        while it:
            new_linked_list.append(it.elem)
            it = it.next
        return new_linked_list
    
    copy = __copy__