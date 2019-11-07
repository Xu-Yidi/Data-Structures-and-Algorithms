### Merge sort
Merge sort和Quick sort同屬Divide-and-conquer(分治法)的應用<br>
- **Logic**<br>
1.***Divide***:如果資料序列*S*只有一個或者0個元素，則無需進行排序；否則將*S*中的元素分別放入兩個子序列*S1*和*S2*中，*S1*和*S2*各占一半元素<br>
2.***Conquer***:遞迴地對*S1*和*S2*進行排序<br>
3.***Combine***:將排序好的*S1*和*S2*進行合併(Merge sort的重點即在於合併)<br>
- **Flowchart**<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week7/merge_sort_flowchart.png">

- **Time complexities**<br>
The running time of mergesort on an input list of size n is **O(nlogn)** in the best, worst, and average case<br>
- **學習歷程**<br>
在理解merge sort的概念後嘗試自主寫出程式，但過程相較heap sort可謂艱難許多，最主要的原因是對遞迴寫法的掌握度不足，最後的做法是只在分割的程式使用了遞迴，其餘使用for迴圈完成，故程式較為冗長，下面首先簡述自己的寫法，然後介紹課本的簡潔寫法<br>
```Python
class Solution(object):
    def merge_sort(self, seq):
        if len(seq) <= 1:        #如果seq的長度為1或0，則無需進行排序
            return seq
        import math
        
        result = self.partition(seq)    #將所有切割過程記錄在result中   
        #長度為n的seq切割成最小單位再進行merge時，有log(n,2)次同一層級的subseq進行合併
        #舉例而言，長度為8的seq，第一次將長度為1的subseq合併，第二次將長度為2的subseq進行合併，第三次將長度為4的subeq合併，log(8,2)=3
        times = math.ceil(math.log(len(seq),2))   
    
        index = []      #記錄result已被合併的subseq的index
        count = 0
        
        #第n次同層級的subseq進行合併時，subseq的長度小於等於2^(n-1)
        #舉例而言，長度為8的seq，第一次合併時subseq的長度為2^0=1，第二次合併時subseq的長度為2^1=2，第三次為2^2=4
        #mer_lenth表示第n次合併時subseq的長度，因為range從0開始，故無需減1
        for mer_lenth in (2**time for time in range(0, times)): 
        
            for i in range(0, len(result)):
                if i not in index:     #如果尚未被合併
                    if len(result[i][0]) <= mer_lenth and len(result[i][1]) <= mer_lenth: #如果subseq的長度小於mer_lenth
                        result[i] = self.merge_seq(result[i][0], result[i][1]) #將兩個subseq合併後的結果取代原本位置的項目
                        index.append(i) #在index記錄索引，表示已被合併
            
            #下述程式的作用是將上一次merge完成的subseq取代下次一merge時對應的subseq
            #舉例而言，長度為4的seq[4,3,2,1]，result中的結果為[[[4],[3]],[[2],[1]],[[4,3],[2,1]]]，
            #第一次merge完為[[3,4],[1,2],[[4,3],[2,1]]]，為進行第二次merge需用[3,4]和[1,2]取代[[4,3],[2,1]]中的[4,3]和[1,2]
            #只需檢查這一層級的subseq，故從count開始
            for i in range(count, len(index)):
                #對應需要取代的subeq一定在其後面，故從其對應的索引後面1位開始搜尋
                for j in range(index[i]+1, len(result)):
                    if j not in index:   #如果尚未被合併
                        if set(result[index[i]]) == set(result[j][0]): #如果合併完成的subseq中元素和某subseq的元素相同
                            result[j][0] = result[index[i]]  #則用合併完的subseq取代此subseq
                            break   #取代完成即跳出迴圈
                        if set(result[index[i]]) == set(result[j][1]):
                            result[j][1] = result[index[i]]
                            break
            
            #因為index中記錄的是所有已被合併的subseq的索引，而在取代時只需檢查這一層級被合併的subseq的索引
            #設定一count變數，其值為此層級merge完成後的index的長度，故下一層級取代時只需檢查下一層合併的subseq，即從conut~len(index)
            count = len(index)
    
        return result[-1] #result中的最後一個subseq即為最終結果
```



