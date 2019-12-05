# Hashing 
Content<br>
[Hash Table](#Hash-Table)<br>
[Hash Functions](#Hash-Functions)<br>
[Collisions](#Collisions)<br>
[Efficiency Analysis](#Efficiency-Analysis)<br>
[Flowchart](#Flowchart)<br>
[Self Learning](#Self-Learning)<br>

## Hash Table
1.The main idea of a **hash table** is to take bucket array, *A*, and a hash function, *h*, and use them to implement a map by storing each item(*key, value*) in the bucket A[*h(key)*].
>哈希表(散列表)，是根據鍵值(key)直接進行訪問的數據結構，即其通過將鍵值映射到表中的某個位置來查找對應的記錄。在此之前，常用的搜尋方法例如線性搜尋法(linear search)或二分搜尋演算法(binary search)都是以比較為基礎的搜尋方法(comparision-based searches)，但以比較為基礎的搜尋演算法其最佳時間複雜度為O(nlogn)，而使用哈希表能提高查詢速度。<br>

2.哈希表 hash table(key, value)將key通過哈希函數(hash function)轉換為儲存數組的index(H(key) = index)，並將對應的key-value pairs儲存於以index為下標的數組空間中，當使用哈希表進行查詢時，則再次使用哈希函數將key轉換為對應的index，並定位到該空間獲取value。<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash_homework.jpg">

## Hash Functions
哈希函數可視為由哈希碼(hash code)與壓縮函數(compression function)兩部分組成，簡單地說，哈希碼將任意類型的資料轉換為整數，而壓縮函數將這一整數壓縮至數組空間位址的區間<br>
1.The goal of a **hash function**, *h*, is to map each key *k* to an integer in the range [0, *N*-1], where *N* is the capacity of the bucket array for a hash table. Equipped with such a hash function, *h*, the main idea of the hash table is to use the hash function value, *h(k)*, as an index into our bucket array, *A*, instead of the key *k*(which may not be appropriate for direct use as an index). That is, we store the item *(k,v)* in the bucket *A[h(k)]*.
>(a)哈希函數將任意長度的輸入或欲映射(preimage)轉換成固定長度的輸出，即將鍵值的集合映射到某個地址集合上<br>
>(b)此種轉換是一種壓縮映，即不同的輸入可能會散列為相同的輸出，從而造成衝突(collision)的現象<br>
>(c)其是一種不可逆的映射(只能單向加密，而無法解密)<br>
>(d)故構造hash table時，不僅需要選擇一個適當的hash function以盡量減少衝突外，還需要解決衝突的問題<br>

2.It's common to view the evaluation of a hash function, *h(k)*, as consisting of two portions, a **hash code** that maps a key *k* to an integer, and a **compression function** that maps the hash code to an integer within the range of indices, [0, *N*-1], or a buckey array.
>The advantage of separating the hash function into two such components is that the hash code of that computation is independent of a specific hash table size. This allows the development of a general hash code for each object that can be used for a hash table of any size; only the compression function depends upon the table size.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash_homework2.gif">

### Hash Codes(哈希碼)
The first action that a hash function performs is to take an arbitrary key *k* in our map and compute an integer that is called the **hash code** for *k*; this integer need not to be in the range [0, *N*-1], and may even be negative<br>
- **Treating the Bit Represention as an integer**<br>
對於數值類型的對象，可簡單的將數值X各位所表示的值作為其hash code，如314的hash code即為314；如果數值的位數超過哈希碼的長度，例如將64位浮點數轉換為32位整數，可對前後32位進行求和或異或(exclusive-or)處理
- **Polynomial Hash Codes**<br>
- **Cyclic-Shift Hash Codes**<br>

### Compression Functions(壓縮函數)
Once we have determined an integer hash code for a key object *k*, there is still the issue of mapping that intger into the range
[0, *N*-1]. This computation, known as a **compression function**, is the second action performed as part of an overall hash function.<br>
- **The Division Method**<br
A simple compressision function is the **division method**, which maps an integer *i* to ***i* mode *N***, where *N*, the size of the bucket, is a fixed positive integer.
>If we take *N* to be a **prime** number, then this compression function helps spread out the distribution of hashed values. Indeed, if *N* is not prime, then there is greater risk that patterns in the distributiom of hash codes will be repeated in the dstribution of hash values, thereby causing collisions.<br>

- **The MAD Method**<br>
A more sophisticated compression function, which helps eliminate repeated patterns in a set of integer keys, is the **Multiple-Add-and-Divide(MAD)** method. This method maps an integer *i* to **[(*ai* + *b*) mod *p*] mod *N***, where *N* is the size of the bucket array, *p* is a **prime** number larger than *N*, and *a* and *b* are integers chosen at random from the interval [0, *p*-1], with *a* > 0.

## Collisions
當鍵值不同，而通過哈希函數轉換後得到的位址相同，即 *k1* != *k2*, *h(k1)* = *h(k2)*, 則會產生衝突，性能良好的哈希函數能夠減少衝突但無法完全避免衝突，故如何解決衝突也是構造和搜尋哈希表的關鍵問題<br>
### Separate Chaining(鏈地址法)
In separate chaining, the hash table is constructed as an array of linked lists. The keys are mapped to an individual index in the usual way, but the item(key, value) are inserted into the linked list referenced from the correspongding entry.
>鏈地址法的基本思想是將所有哈希位址為*i*的item(key, value)構成一個鏈結串列，並將其頭指針儲存於哈希表下標為*i*的位址中，其優點是便於搜尋與刪除，缺點是需要使用額外的空間
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash_homework3.jpg">

### Open Addressing(開放地址法)
Instead of using a list to chain items whose key collide, in open-addressing we attempt to find an alternative location in the hash table for the keys that collide.
>開放地址法的基本思想是，當鍵值key通過哈希函數轉換後得到的位址*p* = *h(key)* 出現衝突時，以*p*為基礎，產生另一個哈希位址*p1*，如果*p1*仍然衝突，再以*p1*為基礎產生另一個哈希位址*p2*，直至找到不衝突的哈希位址*pi*。其函數形式為：*h<sub>i</sub>(key)* = (*h(key)* + d<sub>i</sub>) mod *N*，其中，*N*為哈希表的表長，d<sub>i</sub>為增量序列，增量序列的取值方式不同，相應的再散列方式也不同<br>

[值得注意的是，採用開放地址法時，插入，搜尋，刪除之操作與鏈地址法不同，詳見week11學習筆記之整理(以linear probing為例)](https://github.com/Xu-Yidi/fluteanzi#week11#Basic)
- **Linear Probing**(線性探測再散列)<br>
d<sub>i</sub> = 1, 2, 3,...,*N-1*，即衝突發生時，順序查看哈希表中的下一個位置，直至找出空位置或查遍整個表為止
>eg. key sequence{59,31,3,14,27,41,10,95,67}, the size of hash table is 11, and the hash function is *h(key) = k mode 11*
>*h(59)* = 59 % 11 = 4<br>
>*h(31)* = 31 % 11 = 9<br>
>*h(3)* = 3 % 11 = 3<br>
>*h(14)* = 14 % 11 = 3 / *h<sub>1</sub>(14)* = (3+1) % 4 = 4 / *h<sub>2</sub>(14)* = (3+2) % 14 = 5<br>

Linear probing容易產生**primary clustering**(一次聚集)的現象，即item(key, value)不均勻地佔據hash table，使之後分配到某區塊的item的插入，搜尋，刪除等操作的時間複雜度將受到“前面擋住的item數量”的影響，即某個item需要可能多次查探才能找到對應位置<br>

- **Quadratic probing**(二次探測再散列)<br>
d<sub>i</sub> = 1<sup>2</sup>, -1<sup>2</sup>, 2<sup>2</sup>, -2<sup>2</sup>...,*k*<sup>2</sup>, *-k*<sup>2</sup>(*k*<=*N*/2)，即衝突發生時，在哈希表的前後位置進行跳躍式探測
>eg.(cont.)<br>
>*h(14)* = 14 % 11 = 3 / *h<sub>1</sub>(14)* = (3+1) % 4 = 4 / *h<sub>2</sub>(14)* = (3+ (-1<sup>2</sup>)) % 14 = 5<br>

Quadratic probing可以避免primary clustering的現象，但會產生**secondary clustering**(二次聚集)的現象，即item(key,value)的hash table中的分配仍然並非均勻

### Double Hashing(雙重哈希)
In doublle hashing, when a collision occurs, the key is hashed by a second function *h'* and the result is used as the constant factor in the linear probe. The double hashing techinique is most commomly used to resolve collisions since it reduces both primary and secondary clustering.<br>
>即同時使用多個哈希函數，其函數形式為*h<sub>i</sub>(key)* = (*h(key)* + *i* * *h'* ) mod *N*，其中*h'* 是另一個哈希函數

## Efficiency Analysis
The efficiency of the hash operations depends on the hash function, the size of the table, and the type of probe used to resolve collisions. The time to perform the **search** is the main contributor to the overall time of the three hash table operations:searching, insertions, and deletions.<br>
To evaluate the search performed in hashing, assume there are *n* items currently stored in the table of size *N*. If our hash function is good, then we expect the entries to be uniformly distributed in the *N* cells of the bucket array. Thus, to store *n* entries, the expected numberof keys in a bucket would be *n/N*, which is **O(1)**. In the worst case, a poor hash function could map every item to the same bucket, and this would result in linear-time performance **O(n)**.

***
## Flowchart
作業要求同時使用array與linked list的資料形態，故可得知是使用鏈地址法解決衝突，其插入，刪除，搜尋等操作皆是在linked list中完成，與開放地址法相比較為簡單，但使用較多額外空間<br>
### Add
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash_table_add.jpg">

### Contains
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash_table_contains.jpg">

### Remove
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash_table_remove.png">

## Self Learning
個人學習歷程的部分將對程式碼進行詳細解說
```Python

from Crypto.Hash import MD5            #MD5算法是常用的哈希算法，可視為哈希函數的哈希碼部分

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity   #建立長度為capacity的list
        
    def add(self, key):
        hash_value = self.hash_function(key)
        index = self.add_index(key)
        
        if self.data[index] is None:    #如果下標為index的數組空間為空
            self.data[index] = ListNode(hash_value)  #則將儲存hash_value值的節點直接存於該空間
        else:                           #如果下標為index的數組空間已經有節點
            curNode = self.data[index]  
            while curNode.next is not None:  #不斷向後走訪節點，直至最後一個節點
                curNode = curNode.next
            curNode.next = ListNode(hash_value) #將儲存hash_value值的節點接在最後一個節點後

    def hash_function(self, key):      #hash_function的作用為得到key通過MD5算法轉換後的hash_value
        h = MD5.new()
        h.update(key.encode("utf-8"))  #需指定編碼方式，否則會報錯    
        hash_value = h.hexdigest()
        return hash_value                  
    
    
    def add_index(self, key):          #add_index的作用為得到key插入list中的index
        hash_value = self.hash_function(key)
        #MD5將key轉為16進制的整數，故將其轉為10進制後再對list的長度取餘數以得到index
        index = int(hash_value, 16) % self.capacity  
        return index

    def contains(self, key):
        hash_value = self.hash_function(key)
        index = self.add_index(key)
        
        if self.data[index] is None:   #如果以index為下標的數組空間為空
            return False               #則該key不存在，返回False
        else:                          #如果以index為下標的數組空間不為空
            curNode = self.data[index] 
            while curNode is not None: #不斷向後訪尋節點
                if curNode.val == hash_value: #如果節點的值等於hash_value
                    return True               #則節點存在，返回True(找到第一個即返回)
                else:
                    curNode = curNode.next    #否則繼續向後走訪節點
            return False               #如果走訪到最後一個節點仍未找到，則該key不存在，返回False
            
    def remove(self, key):
        hash_value = self.hash_function(key)
        index = self.add_index(key)
                
        while self.contains(key) is True:  #如果contains函數執行結果為True，即該key仍然存在
            if self.data[index].val == hash_value: #如果linked list頭結點的值即為該key之hash_value
                self.data[index] = self.data[index].next #原來頭結點的後一個節點即為新的頭結點
            else:                          #如果linked list的頭結點與該key無關
                preNode = self.data[index] #儲存比對節點的前一個節點
                curNode = self.data[index].next #真正的比對從頭結點的後一個節點開始
                while curNode is not None:   
                    if curNode.val == hash_value: #如果該節點的值等於hash_value
                        preNode.next = curNode.next #則將該節點前一個節點指向該節點的後一個節點
                        curNode = curNode.next    #比對節點後移一位
                    else:                                                
                        curNode = curNode.next    #否則，curNode與preNode均需後移一位
                        preNode = preNode.next
```
## Reference
1.哈希表（散列表）原理理解 https://blog.csdn.net/duan19920101/article/details/51579136<br>
2.Hash 算法原理詳解 https://blog.csdn.net/tanggao1314/article/details/51457585<br>
3.Hash Tabel(Open Addressing) https://alrightchiu.github.io/SecondRound/hash-tableopen-addressing.html<br>
4.Michael T. Goodrich & Roberto Tamassia &Michael H. Goldwasser. Data Structures and Algorithms in Python.(CH10.2 Hash Tables/P410-421)<br>
