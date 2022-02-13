class Stack():
        def __init__(self):
            self._length = 0
            self._head = None
            
        def __str__(self):
            current = self._head
            result = "Top ->"
            while current:
                result += f"[{current}]"
                current = current.next
            
            result += "<- Bottom"
            return result
            
        def __len__(self):
            return self._length
        
        def __iter__(self):
            self.__iter_item = self._head
            return self
            
        def __next__(self):
            if self.head:
                nxt = self.__iter_item
                self.pop()
                self.__iter_item = self._head
                return nxt
            else:
                raise StopIteration
        
        def push(self, value):
            self._head = Stack_Element(value, self._head)
            self._length += 1
        
        def isEmpty(self):
            return self._length == 0
            
        def pop(self):
            if not self.isEmpty():
                value = self._head.value
                self._head = self._head.next
                self._length -= 1
                return value
            else:
                raise RuntimeError("Stack is empty.")
            
        def peek(self):
            if not self.isEmpty():
                return self._head.value
            else:
                raise RuntimeError("Stack is empty.")
        

class Stack_Element():
    def __init__(self, value, prev):
        self.next = prev
        self.value = value

    def __str__(self):
        return str(self.value)

