# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:43:01 2019

@author: Yidi
"""
"""
說明：以下程式為自行撰寫，但因對遞迴之寫法未達精通之程度，故只在函數partition使用遞迴，而merge_sort的主程式使用了for迴圈的寫法，
雖然程式冗長繁複而較不易理解，但確實符合merge sort的概念以及時間複雜度。merge_sort的程式主要由一個雙層迴圈構成，最外層的迴圈次數為log(n,2)，
內層第一個迴圈為n次，內層的第二個迴圈雖然有兩層，但兩層的執行次數皆十分有限，且會隨著外層次數增加逐漸降低為0，故總時間複雜度仍然近似nlog(n,2)。
"""

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
    
    def merge_seq(self,subseq1, subseq2):   
        merged_seq = [0 for i in range(len(subseq1) + len(subseq2))]  #新建一長度為subseq1和subseq2長度之和的list儲存merge完的元素
        p1 = 0; p2 = 0; q = 0  #p1為subseq1的索引，p2為subseq2的索引，q為merge_seq的索引，並初始化索引為0
    
        #在p1及p2都未超過各自索引的subseq的長度的情況下，比較subseq1[p1]和subseq2[p2],
        #將其中較小的賦值給merge_seq[q]，並將自己的索引及索引q加1
        while p1 < len(subseq1) and p2 < len(subseq2):  
            if subseq1[p1] <= subseq2[p2]:  
                merged_seq[q] = subseq1[p1]
                p1 += 1
            else:
                merged_seq[q] = subseq2[p2]
                p2 += 1
            q += 1
        #如果索引p1大於subseq1的長度而索引p2小於subseq2的長度，說明subseq1中的元素已經比較完成
        #故可直接將subseq2中剩下的元素放入merge_seq
        if p1 >= len(subseq1) and p2 < len(subseq2):
            merged_seq[q:] = subseq2[p2:]
        #同理，若subseq2中的元素已經比較完成，則將subseq1中剩下的元素放入merge_seq
        if p1 < len(subseq1) and p2 >= len(subseq2):
            merged_seq[q:] = subseq1[p1:]
        
        return merged_seq
    
    
    def __init__(self):    #初始化cutseq，否則重複呼叫下面的partition函數會在上一次的cutseq的基礎上進行操作
        self.cutseq = list()
    
    def partition(self, seq):
        if len(seq) > 1: #如果seq的長度大於1，則以中間數進行切割，否則無需切割
            leftseq = seq[:int(len(seq)/2)]
            rightseq = seq[int(len(seq)/2):]
        else:
            return 
        #遞迴地對左右部分進行切割，並將所有切割過程記錄在cuteq中
        self.partition(leftseq)  
        self.partition(rightseq)
        self.cutseq.append([leftseq,rightseq]) 
    
        return self.cutseq
    
output = Solution().merge_sort([-1,54,85,26,24,93,63,63,17,45])
output      
   
#Reference:無任何參考資料，為理解merge sort基本概念後自行寫出
