class StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link
        
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.topNodeA = None
        self.topNodeB = None
    
    def push(self, x: int) -> None:
        self.topNodeA = StackNode(x, self.topNodeA)
        if self.topNodeB is None:
            self.topNodeB = StackNode(x, self.topNodeB)
        else:
            if x <= self.topNodeB.item:
                self.topNodeB = StackNode(x, self.topNodeB)
        
    def pop(self) -> None:
        if self.topNodeA is None:
            return
        else:
            if self.topNodeA.item == self.topNodeB.item:
                self.topNodeB = self.topNodeB.next
            self.topNodeA = self.topNodeA.next
              
    def top(self) -> int:
        if self.topNodeA is None:
            return
        else:
            return self.topNodeA.item
        
    def getMin(self) -> int:
        if self.topNodeA is None:
            return
        else:
            return self.topNodeB.item
                
    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
