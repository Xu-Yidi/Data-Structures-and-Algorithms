### Hashing
**Hashing** is the process of mapping a search key to a limited range of array indices with the goal of providing direct access to the keys. The keys are stored in an array called a **hash table** and a **hash function** is associated with the table. The function converts or maps the search keys to specific entries in the table.<br>
>Example: suppose we have the following set of keys: 765, 431, 96, 142, 579, 226, 903, 388 and a hash table T, containing M = 13 element. We can define a simple hash function h(·) that maps the keys to entries in the hash table: h(key) = key % M, and then we can apply the hash function to these keys, h(765) = 11, h(431) = 2, h(96) = 5, h(142) = 12, h(579) = 7...<br>

<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash1.jpg">

### Basic Procedures
- **Linear Probing**<br>

Consider what happens when we attempt to add key 226 to the hash table, the hash function maps this key to entry 5, but that entry already contains key 96.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash2.jpg">

The result is a **collision**, which occures when two or more keys map to the same hash location. If two keys map to the same table entry, we must resolve the collision by **probing** the table to find another available slot. The simpliest approach is to use a **linear probe**, which examines the table entries in sequential order starting with the first entry immediately following the original hash location. For the key value 226, the linear probe finds slots 6 available, so the key can be stored at that position.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash3.jpg">

When key 903 added, the hash function maps the key to index 6, but we just added kay 226 to this entry. The collision has to be resolved just like any other, by probing to find another slot. In the case of key 903, the linear probe leads to the slot 8.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash4.jpg">

- **Searching**<br>

Searching a hash table for a specific key is very similar to the add operation. The target key is mapped to an intial slot in the table and then it is determined if that entry contains the key. If the key is not at that location, the same probe used to add the keys to the table mustt be used to locate the target. In this case, the probe continues until the target is loacted, a null reference is encountered, or all slots have been examined. When either of the latter two situations occurs, this indicates the target key is not in the table.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash5.jpg">

- **Deletions**<br>

After finding the key, we cannot simply remove it by setting the corresponding table entry to None. Suppose we remove key 226 from our hash table and set the entry at the element 6 to None. And when we perform a search for key 903, the search function will return False, indicating the key is not in the table, even though it's located at element 8.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash6.jpg">

The reason for the unsuccessful search is due to element 6 containing a null reference from that key having been previously removed. Instead of simply setting the corresponding table entry to None, we can use a special flag to indicate the entry is now empty but it had been previously occupied. Thus, when probing to add a new key or in searching for an existing key, we know the search must continue past the slot since the target may be stored beyond this point.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash7.jpg">

