class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._items = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._items.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
        else:
            return self._items.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return
        else:
            return self._items[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._items) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
