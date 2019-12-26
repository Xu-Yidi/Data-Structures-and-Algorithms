## Stack
[code-stack的array與linked list實現](/week3/handout-stack.py)<br>
- **The Stack ADT**<br>
1.inserted and removed according to the ***last-in, first-out(LIFO) principle***<br>
2.***top*** of the stack/ ***base*** of the stack<br>
3.basic operations:<br>
>>(1)**`isEmpty()`**: return a boolean value indicating if the stack is empty<br>
>>(2)**`getSize()`**: returns the number of items in the stack<br>
>>(3)**`pop()`**: remove and returns the top item of the stack, if the stack is not empty, and the next item on the stack becomes the new top item<br>
>>(4)**`push(item)`**: adds the given item to the top of the stack<br>
>>(5)**`peek()`**: returns a reference to the item on top of a non-empty stack without removing it<br>
- **Implementing the Stack**<br> 
1.the stack ADT can be implemented by the use of Python list and a linked list<br>
- **LeetCode**<br>
[#155 min stack](/week3/%23155%20min%20stack.py)<br>

## Queue
[code-circular queue的array與linked list實現&priority queue的array實現](/week3/handout-queue.py)<br>
- **The Queue ADT**<br>
1.items can only be added to one end and removed from the other, known as the ***first-in, first-out(FIFO)principle***<br>
2.new items are inserted into a queue at the ***rear*** while existing items are removed from the ***front***<br>
3.basic operations:<br>
>>(1)**`isEmpty()`**: return a boolean value indicating whether the queue is empty<br>
>>(2)**`getSize()`**: returns the number of items currently in the queue<br>
>>(3)**`enqueue(item)`**: adds the given item to the back of the queue<br>
>>(4)**`dequeue()`**: removes and returns the front item from the queue, an item can not be dequeued from an empty queue<br>
>>(5)**`getFront()`**: return a reference to the element at the front of queue without removing it, and an error occurs if the queue is empty<br>
>>(6)**`getRear()`**: return a reference to the element at the back of queue without removing it<br>
- **Implementing the Queue**<br>
1.implementation of the Queue ADT using a Python list<br>
2.**using a circular array**<br>
(1)a circular array is simply an array viewed as a circle instead of a line<br>
(2)allows to add new items to a queue and remove existing ones without having to shift items in the process<br>
(3)introduces the concept of a ***maximum-capacity queue*** that can become full<br>
(4)uesd with application that require small-capacity and allows for the specification of a maximum size<br>
(5)must maintain a count field and two markers:<br>
>>a.***count field***: to keep track of how many items are currently in the queue<br>
>>b.***front and rear***: to indicate the array elements containing the first and last items in the queue<br>
- **The Priority Queue**<br>
1.a priority queue is a queue with each item is assigned a priority and items with a high priority are removed before those with lower priority<br>
(1)***the bounded priority queue*** assumes a small limited range of p priorities over the interval of integers[0,p)<br>
(2)***the unbounded priority queue*** places no limit on the range of integer values that can be used as priorities<br>
(3)integer values are used for the priorities with a smaller integer value having a higher pripority<br>
2.basic operations:<br>
>>(1)**`PriorityQueue()`**: creates a new empty unbounded priority queue<br>
>>(or 1)**`BPriorityQueue(numLevels)`**: creates a new empty bounded priority queue with priority levels in the range from 0 to numLevels-1<br>
>>(2)**`isEmpty()`**<br>
>>(3)**`getSize()`**<br>
>>(4)**`enqueue(item, priority)`**: adds the given item to the queue by inserting it in the proper position based on the given pripority<br>
>>(5)**`deququq()`**: removes and returns the front item from the queue, which is the item with the highest priority,if two items have the same priority, then items are removed with FIFO order<br>
- **LeetCode**<br>
[#232 implement queue using stacks](/week3/%23232%20implement%20queue%20using%20stacks.py)<br>
[#622 design circular queue](/week3/%23622%20design%20circular%20queue.py)<br>
