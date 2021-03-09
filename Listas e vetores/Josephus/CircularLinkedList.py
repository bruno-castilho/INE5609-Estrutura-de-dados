
class CircularLinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt
        
    def __init__(self):
        self._tail = None
        self._size = 0

    
    def __len__(self):
        return self._size

    
    def _get(self, elem):
        if self._tail is None:
            return None
        pivot = self._tail._next
        while(pivot != self._tail and pivot._element != elem):
            pivot = pivot._next

        if pivot._element != elem:
            return None
        
        return pivot

    def _remove(self, pivot):
        if self._size == 1 or self.is_empty():
            self._tail = None
            self._size = 0
        else:
            if pivot._next == self._tail:
                self._tail = pivot
            pivot._next = pivot._next._next
            self._size -= 1
        
    def is_empty(self):
        return self._size == 0
    
    def get(self, elem):
        result = self._get(elem)
        if result is None:
            return None
        return result
    
    def push(self, elem):
        new_node = self._Node(elem, None)

        if self.is_empty():
            self._tail = new_node
            self._tail._next = self._tail
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node

        self._size += 1
    
    def __str__(self):
        if self.is_empty():
            return str([])
        to_print = []
        pivot = self._tail._next
        while pivot != self._tail:
            to_print.append(pivot._element)
            pivot = pivot._next
        to_print.append(pivot._element)
        return str(to_print)




