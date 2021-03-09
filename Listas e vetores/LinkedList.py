class LinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__ (self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__ (self):
        self._head = None
        self._size = 0

    def __len__ (self):
        return self._size

    def _get (self, elem):
        pivot = self._head

        while (pivot != None and pivot._element != elem):
            pivot = pivot._next
        
        return pivot

    def is_empty(self):
        return self._size == 0

    def get(self, elem):
        result = self._get(elem)

        if result is None:
            return None
        return result
    
    def insert (self, elem, pos):
        new_node = self._Node(elem, None)
        if (pos == 0):
            new_node._next = self._head
            self._head = new_node
        else:
            insert_here = self._head
            idx = 1

            while idx < pos:
                insert_here = insert_here._next
                idx += 1
            new_node._next = insert_here._next
            insert_here._next = new_node
        self._size += 1

    def remove(self, pos):
        if pos == 0:
            value = self._head._element
            self._head = self._head._next
        else:
            remove_next = self._head
            idx = 1

            while idx < pos:
                remove_next = remove_next._next
                idx += 1
            value = remove_next._next._element
            remove_next._next = remove_next._next._next

        self._size -= 1

        return value
    
    def __str__(self):
        to_print = []
        pivot = self._head
        while pivot is not None:
            to_print.append(pivot._element)
            pivot = pivot._next
        return str(to_print)
    






