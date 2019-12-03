## Hashing 
### Hash Table
1.A **hash table** (or **hash map**) is a data structure that uses a hash function to efficiently map keys to values, to efficient search and retrieval.<br>
>哈希表(散列表)，是根據鍵值(key value)直接進行訪問的數據結構，即其通過將鍵值映射到表中的某個位置來查找對應的記錄。在此之前，常用的搜尋方法例如線性搜尋法(linear search)或二分搜尋演算法(binary search)都是以比較為基礎的搜尋方法(comparision-based searches)，但以比較為基礎的搜尋演算法其最佳時間複雜度為O(nlogn)，而使用哈希表能提高查詢速度。<br>

2.哈希表 hash table(key, value)將key通過哈希函數(hash function)轉換為儲存數組的index(H(key) = index)，並將對應的key-value pairs儲存於以index為下標的數組空間中，當使用哈希表進行查詢時，則再次使用哈希函數將key轉換為對應的index，並定位到該空間獲取value。<br>

### Hash Functions


















### Reference
1.哈希表（散列表）原理理解 https://blog.csdn.net/duan19920101/article/details/51579136<br>

