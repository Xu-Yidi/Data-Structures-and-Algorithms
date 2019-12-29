# Graph
因為本文撰寫過程中使用LATEX公式，故閱讀前請先安裝[mathjax plugin for github](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima?hl=en)
## Shortest Path(最短路徑)
### Weighted Graph
A **weighted graph** is a graph that has a numeric label *w(e)* associated with each edge *e*, called the **weight** of edge *e*<br>

### Dijkstra's Algorithm
#### Greedy Method(貪心策略)
The greedy method applies to **optimization** problems with the following pattern: Starting from a suitable starting condition, a sequence of **locally** optimal choices produces a **globally** optimal solution. This method does not always lead to an optimal solution, but there are several problems that it does work for, and such problems are said to possess the **greedy-choice** property. That is the property that a global optimal condition can be reached by a series of locally optimal choices starting froma a well-defined starting condition.  <br>
貪心策略是尋找最優解問題的常用方法，這種方法將求解過程分成若干步驟，每個步驟都選取當前狀態下最優選擇(局部最優)， 並希望最終堆疊出的結果是全局最優結果，但貪心策略有時無法得到全局最優解<br>

#### Detailed Process
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week14%2615/Dijkstra.jpg">

step1: 假設起始頂點為0，依據adjacency matrix得到頂點0與其他頂點的距離;<br>
step2: 將頂點1加入，則頂點0至頂點0、1的距離維持不變，又從adjacency matrix可知，頂點1與頂點3、4、5、6、8皆不鄰接，故也無需更動；但頂點1與頂點2、7鄰接，則需要比較原距離與新距離，原先頂點0無法到達頂點2，現在可通過頂點1到達，距離為頂點0至頂點1距離加上頂點1至頂點2距離，更動距離為4+8=12，原先頂點1至頂點7之距離為8，通過頂點1到達頂點7之距離為4+11=15，大於原先的距離8，故不需改動;<br>
step3: 加入頂點7，則頂點0至頂點0、1、7的距離不變，又頂點7與頂點2、3、4、5皆不鄰接，故同樣無需更動，但頂點7與頂點6、8鄰接，頂點0原本無法到達頂點6與頂點8，現在可通過頂點7到達，距離為頂點0到頂點7之距離加上頂點7到頂點6、8的距離，分別為8+1=9及8+7=15;<br>
step4: 加入頂點6，則頂點0至頂點0、1、7、6的距離不變，又頂點6與頂點2、3、4皆不鄰接，故無需更動，但頂點6與頂點5、8鄰接，原本頂點0無法到達頂點5，現在可通過頂點6到達頂點5，更動距離為9+2=11，原本頂點0到頂點8之距離為15，通過頂點6到達頂點8之距離同樣為9+6=15，故無需更動;<br>
step5: 以此類推，不斷加入頂點，直至計算出頂點0至所有其他頂點的最短路徑

#### Time Complexities

## Minimum Spanning Tree(最小生成樹)
### Problem Definition
Give an undirected, weighted graph, *G*, we are interested in finding a tree *T* that contians all the vertices in *G* and minimizes the sum
$$
w(T) = \sum_{(u, v)\in T} w(u, v)
$$
A tree, such as this, that contains every vertex of a connected graph *G* is said to be a **spanning tree**, and the problem of computing a spanning tree *T* with smallest total weight is known as the **minimun spanning tree(MST)** problem.

### Kruskal's Algorithm
#### Disjoint Set(並查集)
Disjoint-set data structure is a data structure representing a dynamic collection of sets $\mathbf{S} = \{S_1,...,S_n\}$. Given an element *u*, we denote by $S_u$ the set containing *u*. We will equip each set $S_i$ with a representive element $rep[S_i]$. This way, checking whether two elements *u* and *v* are in the same set amounts to checking whether $rep[S_u] = rep[S_v]$. The disjoint-set data structure supports the following operations:<br>
- MakeSet(*u*): Creates a new set containing the single element *u* <br>
    - *u* must not belong to any already existing set<br>
    - *u* will be the representive element initially<br>

- FindSet(*u*): Returns the representive $rep[S_u]$<br>
- Union(*u*, *v*): Replace $S_u$ and $S_v$ with $S_u \cup S_v$ in $\mathbf{S}$. Updates the representive elements as appropriate<br>

#### Detailed Process
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week14%2615/Kruskal.jpg">


step1: 首先將所有edge按weight從小至大排序，在初始情況下，disjoint set中每個頂點各自為一個set，且為各自的代表元素，故每個頂點的parent皆為自身;<br>
step2: 判斷edge(7, 6)是否應該加入，$rep[S_7] = 7$，$rep[S_6] = 6$，故頂點7與頂點6分屬不同的set，故可加入edge(7, 6)，按照從左至右的原則(可以自己決定)合併$S_7$與$S_6$，將7作為代表元素，即$rep[S_7] = rep[S_6] = 7$;<br>
step3: 判斷edge(8, 2)是否應該加入，原理同上，合併$S_8$與$S_2$，並將8作為代表元素，即$rep[S_8] = rep[S_2] = 8$;<br>
step4: 判斷edge(6, 5)是否應該加入，$rep[S_6] = 7$，$rep[S_5] = 5$，故頂點6與頂點5分屬不同的set，故可加入，6應是5的代表元素，但因7是6的代表元素，故5的代表元素也是7，即合併$S_6$與$S_5$，$rep[S_7] = rep[S_6] = rep[S_5] = 7$;<br>
step5: 判斷edge(0, 1)是否應該加入，同上合併$S_0$與$S_1$，並將0作為代表元素，即$rep[S_0] = rep[S_1] = 0$;<br>
step6: 判斷edge(2, 5)是否應該加入，$rep[S_2] = 8$，$rep[S_5] = 7$，兩頂點分屬不同set，故可加入，2應是5的代表元素，而8是2的代表元素，故5的代表元素應從7改為8，且之前以7位代表元素的頂點其代表元素都應改為8，即合併$S_2$與$S_5$，$rep[S_8] = rep[S_2] = rep[S_7] = rep[S_6] = rep[S_5] = 8$;<br>
step7: 判斷edge(8, 6)是否應該加入，$rep[S_8] = rep[S_6] = 8$，即頂點8與頂點6屬於同一個set，故不應該加入edge(8, 6);<br>
step8: 以此類推，判斷其餘的edge是否應該加入，當挑出的**edge數量為頂點數量減1**時，即可停止，舉例而言，連接3個頂點而不形成迴路需要2條邊，連接5個頂點不形成迴路需要4條邊<br>
#### Time Complexities

## Self Learning
### Flowchart
Dijsktra<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week14%2615/dijsktra_flowchart.jpg" height=80%>

Kruskal<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week14%2615/Kruskal_flowchart.jpg" height=80%>


### Code
Dijsktra<br>
```Python
class Graph():    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)] for row in range(vertices)]
    
    
    def Dijkstra(self, s):
        #以字典的形式儲存起始頂點s至其他頂點的距離，且type(key) = string
        dis_dict = dict(zip([str(i) for i in range(self.V)], self.graph[s])) 
        #print(dis_dict)
        add_vertex = [str(s)]    #建立add_vertex以儲存已經加入之頂點
        
        while True:
            vertex = self.getKey(dis_dict, add_vertex)  #type(vertex): string 
            #print(vertex)
            if vertex is False:  #如果尋找最短路徑已經完成或餘下孤點，則跳出while迴圈
                break
          
            add_vertex.append(vertex)
            
            #找出與此次加入之頂點相鄰接且尚未加入之頂點
            adj_vertices = [str(i) for i in range(self.V) if str(i) not in add_vertex and self.graph[int(vertex)][i] != 0]
            #type(adj_vertex):string
            
            for i in adj_vertices:
                if dis_dict[i] == 0:  #如果起始頂點尚無法到達鄰接點
                    #則起始頂點與鄰接點的距離為起始頂點與新加入頂點之距離加上新加入頂點與鄰接點的距離
                    dis_dict[i] = dis_dict[vertex] + self.graph[int(vertex)][int(i)] 
                else:                 #如果起始頂點可到達鄰接點，則比較原距離與新距離之大小
                    if dis_dict[vertex] + self.graph[int(vertex)][int(i)] < dis_dict[i]:
                        dis_dict[i] = dis_dict[vertex] + self.graph[int(vertex)][int(i)]
            #print(dis_dict)
        
        return dis_dict
  
    
    def getKey(self, dis_dict, add_vertex):      #getKey函數之作用是找出下一個加入之頂點
        value = []                               
        for i in range(self.V):
            if str(i) not in add_vertex:  #如果頂點尚未加入
                value.append(dis_dict[str(i)])   
       
        while 0 in value:    #距離為0代表無法到達，故需刪除             
            value.remove(0)
        
        if value == []:      #如果value為空，可能(1)所有頂點都已經加入，則尋找最短路徑完成
            return False     #(2)起始頂點到某些頂點的值仍為0，即這些頂點為孤點
        
        for key in dis_dict.keys():     
            if dis_dict[key] == min(value): #找出並返回下一個加入的頂點，即與起始頂點距離最近(≠0)且尚未加入之頂點
                return key
```
Kruskal
```Python
from collections import defaultdict

class Graph():    
    
    def __init__(self, vertices):
        self.V = vertices
        #以字典的形式儲存edge及其權重，例如{(0,1):4, (0,7):8}
        self.graph_list = defaultdict(dict)  
        self.vertices = set() #以集合的形式儲存所有頂點，避免重複記錄

    
    def addEdge(self, u, v, w):
        self.graph_list[(u,v)] = w
        self.vertices.add(u)
        self.vertices.add(v)


    def Kruskal(self):
        #以weight為標準對所有edge進行升序排序，排序完成後以tuple的形態儲存於list中，如[((6, 7), 1), ((2, 8), 2), ((5, 6), 2)]
        edge_sort = sorted(self.graph_list.items(), key = lambda item: item[1])
        #print(edge_sort)
        
        disjoint_set = [[i] for i in self.vertices]  #makeSet: 將所有頂點各自形成一個set
        
        result = []   #儲存最後構成MST的edge
        
        for edge in edge_sort:
            #如果構成edge的兩個頂點來自不同的set，則加入這條邊
            if self.findSet(disjoint_set, edge[0][0], edge[0][1]) is True:
                result.append(edge)
                disjoint_set = self.mergeSet(disjoint_set, edge[0][0], edge[0][1]) #合併edge頂點所屬的兩個set
        
        edge_dict = {}  #將result中之結果整理為要求之字典形式
        for edge in result:
            key = str(edge[0][0]) + '-' + str(edge[0][1])
            edge_dict[key] = edge[1] 
 
        return edge_dict
                
    
    def findSet(self, disjoint_set, u, v): #findSet函數主要功能為判斷頂點u,v是否來自同一個 set
        rep_u, rep_v = -1, -1
       
        for _set in disjoint_set:
            if u in _set:
                rep_u = _set[0]   #rep_u為頂點u所屬set的代表元素，取第一個元素
        for _set in disjoint_set:
            if v in _set:
                rep_v = _set[0]  #rep_v為頂點v所屬set的代表元素，取第一個元素
        #print(rep_u, rep_v)
        
        if rep_u == rep_v:       #如果rep_u與rep_v相等，說明頂點u,v來自同一個set，返回False
            return False
        else:                    #否則，返回True
            return True

        
    def mergeSet(self, disjoint_set, u, v): #mergeSet函數主要功能為合併兩個set
        set_u, set_v = [], []

        for _set in disjoint_set:
            if u in _set:
                set_u = _set     #以set_u暫存頂點u所屬的set
                disjoint_set.remove(_set)  #移除頂點u所屬的set
                break
        for _set in disjoint_set:            
            if v in _set:
                set_v = _set     #以set_v暫存頂點v所屬的set
                disjoint_set.remove(_set)   #移除頂點v所屬的set
                break
        
        set_u = set_u + set_v    #將兩個set合併為一個
        #合併遵照從左至右的規則，舉例而言，給定邊((7, 6), 1)，合併後為[7, 6]，再給定((6, 5), 1)，合併後為[7, 6, 5]
        disjoint_set.append(set_u) #加入合併完後的set
        #print(disjoint_set)
        return disjoint_set
```

**Reference**
1. Michael T. Goodrich & Roberto Tamassia &Michael H. Goldwasser. *Data Structures and Algorithms in Python.*<br>
2. https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec16.pdf<br>
 
