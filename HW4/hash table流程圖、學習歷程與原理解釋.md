# Hashing 
## Hash Table
1.A **hash table** (or **hash map**) is a data structure that uses a hash function to efficiently map keys to values, to efficient search and retrieval.<br>
>哈希表(散列表)，是根據鍵值(key)直接進行訪問的數據結構，即其通過將鍵值映射到表中的某個位置來查找對應的記錄。在此之前，常用的搜尋方法例如線性搜尋法(linear search)或二分搜尋演算法(binary search)都是以比較為基礎的搜尋方法(comparision-based searches)，但以比較為基礎的搜尋演算法其最佳時間複雜度為O(nlogn)，而使用哈希表能提高查詢速度。<br>

2.哈希表 hash table(key, value)將key通過哈希函數(hash function)轉換為儲存數組的index(H(key) = index)，並將對應的key-value pairs儲存於以index為下標的數組空間中，當使用哈希表進行查詢時，則再次使用哈希函數將key轉換為對應的index，並定位到該空間獲取value。<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week11/hash_homework.jpg">

## Hash Functions: hash codes followed by compression functions
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
- **The Division Method**<br>
A simple compressision function is the **division method**, which maps an integer *i* to *i* mode *N*, where *N*, the size of the bucket, is a fixed positive integer.
>If we take *N* to be a **prime** number, then this compression function helps spread out the distribution of hashed values. Indeed, if *N* is not prime, then there is greater risk that patterns in the distributiom of hash codes will be repeated in the dstribution of hash values, thereby causing collisions.<br>
























### Reference
1.哈希表（散列表）原理理解 https://blog.csdn.net/duan19920101/article/details/51579136<br>
2.Hash 算法原理詳解 https://blog.csdn.net/tanggao1314/article/details/51457585<br>
