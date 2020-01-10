## LeetCode
ps. 之前根據課程要求已完成了206/707155/232/147/705/912等題，以下為不在課綱要求之題目
### Q.24 Swap Nodes in Pairs
- Difficulty: Medium<br>
- Example: <br>
input: 1→2→3→4→5→6<br>output: 2→1→4→3→6→5
- Hint:<br>
```Python
tempVal = curNode.val
curNode.val = curNode.next.val
curNode.next.val = tempVal
curNode = curNode.next.next
```

### Q.143 Reorder List
- Difficulty: Medium<br>
- Example: <br>
input: 1→2→3→4→5→6<br>output: 1→6→2→5→3→4
- Hint:將節點的值儲存於list中，再使用index間的關係重新構建
```python
self.addNode(ListNode(stack[index]))
self.addNode(ListNode(stack[len(stack)-1-index]))
```

### Q.622 Design Circular Queue
- Difficulty: Medium<br>
- Example<br>
- Hint: 題目規定了queue的capacity，故應該是使用array而非linked list進行實作，其關鍵在於enqueue與dequeue時front與rear的變動
```python
self._rear = (self._rear + 1) % len(self._items)
self._front = (self._front + 1) % len(self._items)
```

### Q.704 Binary Search
- Difficulty: Easy<br>
- Example: 給定已排序且無重複值的list如[1,3,4,5,6,8,9]，目標為4，list的中間值為5，其比4大，故繼續找左邊[1,3,4]的中間值3，其比3小，故繼續向右邊[4]找中間值，其即為答案
- Hint: 使用遞迴
```python
 def searchHelper(self, nums, target, index):
    return self.searchHelper(nums[:mid], target, idx-(less_length+2)//2)
    return self.searchHelper(nums[mid+1:], target, idx+(larger_length+1)//2)
```

### Q.876 Middle of the Linked List
- Difficulty: Easy<br>
- Example<br>
input: 1→2→3→4→5→6<br>output: 4→5→6
- Hint: 先求出linked list的長度，再向後走長度的一半即可
