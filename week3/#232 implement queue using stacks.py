class QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = None
        self.rear = None
        self.count = 0
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        node = QueueNode(x)
        if self.empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.count += 1        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
        node = self.front
        self.front = self.front.next
        self.count -= 1
        return node.item        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return
        return self.front.item
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.count == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
