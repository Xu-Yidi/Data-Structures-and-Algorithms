# **Data Structure and Algorithm in Python資料結構與演算法**

此處文件包含自行整理之資料結構的handout與Leetcode的程式，handout包含資料結構的基本特性的描述（以註解方式給出）以及基本操作的Python程式

## week2
### **Singly Linked List**<br>

**Linked List**<br>
1.A linked structure contains a collection of objects called nodes, each of which contains data and at least one reference or link to another node<br>
2.A linked list is a structure in which the nodes are connected in sequence to form a linear list<br>
(1)The first node in the list(head node), must be named or referenced by external variable<br>
(2)The last node in the list(tail node), is indicated by a null link reference<br>
(3)A linked list can be empty, which can be indicated when the head reference is null<br>

**The Singly Linked List**<br>
1.A singly linked list is a linked list in which each node contains a single link field and allows for a complete traversal from a distinctive first node to the last<br>


## week3
### Stack
1.inserted and removed sccording to the ***last-in, first-out(LIFO) principle***<br>
2.***top*** of the stack/ ***base*** of the stack<br>
3.basic operations:<br>
(1)**`isEmpty()`**: returna boolean value indicating if the stack is empty<br>
(2)**`getSize()`**: returns the number of items in the stack<br>
(3)**`pop()`**: remove and returns the top item of the stack, if the stack is not empty, and the next item on the stack becomes the new top item<br>
(4)**`push(item)`**: adds the given item to the top of the stack<br>
(5)**`peek()`**: returns a reference to the item on top of a non-empty stack without removing it<br>
4.the stack ADT can be implemented by the use of Python list and a linked list

### Queue
- **The Queue ADT**<br>
1.items can only be added to one end and removed from the other, known as the ***first-in, first-out(FIFO)principle***<br>
2.new items are inserted into a queue at the ***rear*** while existing items are removed from the ***front***<br>
3.basic operations:<br>
(1)**`isEmpty()`**: return a boolean value indicating whether the queue is empty<br>
(2)**`getSize()`**: returns the number of items currently in the queue<br>
(3)**`enqueue(item)`**: adds the given item to the back of the queue<br>
(4)**`dequeue()`**: removes and returns the front item from the queue, an item can not be dequeued from an empty queue<br>
(5)**`getFront()`**: return a reference to the element at the front of queue without removing it, and an error occurs if the queue is empty<br>
(6)**`getRear()`**: return a reference to the element at the back of queue without removing it<br>
- **Implementing the Queue**<br>
1.implementation of the Queue ADT using a Python list<br>
2.**Using a Circular Array**<br>
(1)a circular array is simply an array viewed as a circle instead of a line
(2)allows to add new items to a queue and remove existing ones without having to shift items in the process
(3)introduces the concept of a maximum-capacity queue that can become full
(4)uesd with application that require small-capacity and allows for the specification of a maximum size
(5)must maintain a count field and two markers:
a.count field: to keep track of how many items are currently in the queue
b.front and rear: to indicate the array elements containing the first and last items in the queue

<img width="175" height="175" src="http://img.wxcha.com/file/201712/06/9a3fc5676a.jpg"/>
