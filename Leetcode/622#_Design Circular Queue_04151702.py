class MyCircularQueue:

    def __init__(self, k: int):
        self._front = 0
        self._rear = k - 1
        self._count = 0
        self._items = [None] * k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self._rear = (self._rear + 1) % len(self._items)
            self._items[self._rear] = value
            self._count += 1
            return True       

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self._items[self._front] = None
            self._front = (self._front + 1) % len(self._items)
            self._count -= 1
            return True
            
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._items[self._front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._items[self._rear]
        
    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == len(self._items)
