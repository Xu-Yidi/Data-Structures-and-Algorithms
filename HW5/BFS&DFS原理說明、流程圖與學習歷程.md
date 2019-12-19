# Graph
在介紹BFS與DFS的定義前，首先應對圖(Graph)的概念有所了解，故本文會首先說明資料結構中的圖形結構與其基本表達方式，可從目錄直接閱讀圖的訪尋部分<br>
### PS:因文中在鄰接矩陣等處使用了LATEX公式，故若要顯示公式請先安裝[MathJax Plugin for Github](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima)

**Content**<br>
[Graphs](#Graphs)<br>
[Some Concepts](#Some-Concepts)<br>
[Data Structures for Graphs](#Data-Structures-for-Graphs)<br>
&#160; &#160; &#160;[Adjacency Matrix](#Adjacency-Matrix)<br>
&#160; &#160; &#160;[Adjacency List](#Adjacency-List)<br>
&#160; &#160; &#160;[Incidence Matrix](#Incidence-Matrix)<br>
[Graph Traversal](#Graph-Traversal)<br>
&#160; &#160; &#160;[Breadth-First Search](#Breadth-First-Search)<br>
&#160; &#160; &#160;[Depth-First Search](Depth-First-Search)

## Graphs(圖)
A **graph** *G = (V, E)* is simply a set *V* of **vertices**（頂點) and a collection *E* of pairs of vertices from *V*, called **edges**(邊). Thus, a graph is a way of represnting connections or relationships between pairs of objects from some set *V*<br>
### Undirected Graph(無向圖)
An edge *(u,v)* is said to be **directed** from *u* to *v* if the pair *(u,v)* is ordered, with *u* preceding *v*. If all the edges in a graph are undirected , then we say the graph is an **undirected graph**.

### Directed Graph(有向圖)
An edge *(u,v)* is said to be **undirected** if the pair *(u,v)* is not ordered. If all the edges in a graph are undirected, then we say the graph is an **undirected graph**.

>Ex.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week12%2613/graph1.jpg">

>G<sub>1</sub>(undirected graph)<br>
>V(G<sub>1</sub>) = {1,2,3,4,5}<br>
>E(G<sub>1</sub>) = {(1,2),(1,3),(1,5),(2,3),(2,5),(3,4)}<br>
>G<sub>2</sub>(directed raph)<br>
>V(G<sub>2</sub>) = {1,2,3,4,5}<br>
>E(G<sub>1</sub>) = {<1,2>,<1,5>,<5,1>,<2,3>,<3,1>,<3,4>,<4,3>}<br>

### Mixed Graph
A graph that has both directed and undirected edges is often called a **mixed graph**. Note that an undirected or mixed graph can be converted into a directed graph by replacing every undirected edge *(u,v)* by the pair of directed edges *(u,v)* and *(v,u)*.

## Some Concepts
1.**End Vertices**: The two vertices joined by an edge are called the **end vertices** of the edge. If an edge is directed, its first endpoints is its **origin** and other is the **destination** of the edge.<br>
2.**Adjacent**(鄰接): Two vertices *u* and *v* are said to be **adjacent** if there is an edge whose end vertices are *u* and *v*.<br>
3.**Incident**(關聯): An edge is said to be **incident** to a vertex if the vertex is one of the edge's endpoints.<br>
4.**Outcoming/Incoming Edge**(出邊/入邊): The outgoing edges of a vertex are the directed edges whose origion/destination is that vertex.<br>
5.**In-degree/Out-degree**(入支度/出支度): The **in-degree** and **out-degree** of a vertex *v* are the number of incoming and outgoing edges of *v*.<br>
6.**Degree**(分支度): The degree of vertex *v*, is the number of incident edges of *v*.<br>
7.**path**(路徑): A path is a sequence of alternating vertices and edges that starts at a vertex and ends at a vertex such that each edge is incident to its predecessor and successor vertex.<br>
8.**Cycle**(循環): A cycle is a path that starts and ends at the same vertex, and that includes at least one edge.<br>
9.**Simple**: A path is **simple** if each vertex in the path is distinct, and we say that a cycle is **simple** if each vertex in the cycle is distinct, except for the first and last one.<br>
10.**Connected Graph**(相連圖形): A graph is **connected** if, for any two vertices, there is a path between them.<br>
11.**Subgrapg**(子圖): A **subgraph** of a graph *G* is a graph *H* whose vertices and edges are subsets of the vertices and edges of *G*, respectivly.<br>

## Data Structures for Graphs
### Adjacency Matrix
The **adjacency matrix**(鄰接矩陣) *A(G)* for a graph *G = (E, V)* with n vertices is a *n × n* matrix whose *A(i,j)* entry is 1 if the *i<sup>th</sup>* vertex and *j<sup>th</sup>* vertex are connected, and 0 if they are not. Note that matrix *A* is symmetric if graph *G* is undirected, as *A(i,j)* = *A(j,i)* for all pairs of *i* and *j*.

$$
A[i,j]=
\begin{cases}
1, & if (V_i,V_j)\in E(G),\\\\
0, & if (V_i,V_j)\notin E(G)
\end{cases}
$$

Ex:<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week12%2613/graph1.jpg">

$$
A(G_1) =
\left[ \begin{matrix}
	0 & 1 & 1 & 0 & 1 \\\\
	1 & 0 & 1 & 0 & 1 \\\\
	1 & 1 & 0 & 1 & 0 \\\\
	0 & 0 & 1 & 0 & 0 \\\\
	1 & 1 & 0 & 0 & 0
\end{matrix}\right]
A(G_2)=
\left[ \begin{matrix}
	0 & 1 & 0 & 0 & 1 \\\\
	0 & 0 & 1 & 0 & 1 \\\\
	1 & 0 & 0 & 1 & 0 \\\\
	0 & 0 & 1 & 0 & 0 \\\\
	1 & 0 & 0 & 0 & 0
\end{matrix}\right]
$$

### Adjacency List
The **adjacency list**(鄰接表) structure groups the edges of a graph by storing them in smaller, secondary containers that are associated with each individual vertex.<br>
當頂點個數很多而邊數較少時，鄰接矩陣的儲存方式將造成儲存空間的浪費，而鄰接表使用數組與鏈結串列結合的方式，將頂點儲存在一維數組中，並將頂點的鄰接點儲存在鏈結串列中
>Ex: undirected graph(cont.)<br>
>[1]→[2]→[3]→[5]<br>
>[2]→[1]→[3]→[5]<br>
>[3]→[1]→[2]→[4]<br>
>[4]→[3]<br>
>[5]→[1]→[2]<br>
>Ex: directed graph(cont.)<br>
>[1]→[2]→[5]<br>
>[2]→[5]→[3]<br>
>[3]→[1]→[4]<br>
>[4]→[3]<br>
>[5]→[1]
### Incidence Matrix
The (vertex-edge) **incidence matrix**(關聯矩陣) *I(G)* of a grapg *G = (E, V)*, is a *n × m* matrix defined as follows. The rows and columns of *I(G)* are indexed by *V(G)* and *E(G)*, respectively. The *A(i,j)* entry of *I(G)* is 0 if vertex v<sub>i</sub> and and edge e<sub>j</sub> are not incident, and otherwise it is 1 or -1 according as e<sub>j</sub> originates or terminates at i, respectively.<br>

$$
I[i,j]=
\begin{cases}
1, & if \ v_i \ is \ the \ origin \ of \ e_j,\\\\
-1, & if \ v_i \ is \ the \ destination \ of \ e_j,\\\\
0, & if \ e_i \ and \ v_i \ are \ not \ incident
\end{cases}
$$

Ex.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week12%2613/graph2.jpg">
$$
I(G)=
\left[ \begin{matrix}
    -1 & 1 & -1 & 0 & 0 & 0 \\\\
	1 & 0 & 0 & -1 & 0 & 0 \\\\
	0 & -1 & 0 & 0 & 1 & 0 \\\\
	0 & 0 & 1 & 0 & 0 & -1 \\\\
	0 & 0 & 0 & 1 & -1 & 1
\end{matrix}\right]
$$

## Graph Traversal
### Breadth-First Search
廣度優先搜尋從起始頂點*v*開始走訪，接著依序訪尋**所有**與起始頂點*v*相鄰但未走訪的頂點，依照此法不斷擴展，走訪與起始頂點的鄰接點相鄰接的所有頂點，直至訪尋完全部頂點，簡而言之為先廣後深<br>
#### 解法 
BFS的實作需要使用**佇列(queue)**的資料結構，且在訪尋的過程中需要記錄頂點的狀態，示意圖中使用1表示尚未走訪且尚未放入queue中的頂點，2表示尚未走訪但已放入queue中的頂點，3表示已訪尋過的頂點。首先，假設頂點*v1*為起始頂點，將*v1*放入queue，訪尋*v1*後，將*v1*從queue中刪除，並根據鄰接表將*v1*的鄰接點依序加入queue，**但放入的鄰接點需為未訪尋過也尚未在queue中的頂點**，即狀態為1的頂點，故將*v2*和*v5*加入queue。依據queue先進先出的原則，下一個訪尋的頂點為*v2*，同理，將*v2*從queue中刪除，並將其鄰接點*v3*和*v4*依序加入queue。以此類推，直至queue為空，則完成BFS走訪。
#### 圖示
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week12%2613/bfs.jpg">

### Depth-First Search
深度優先搜尋先訪問圖中某個起始頂點*v*，然後訪問與*v*鄰接且未被訪問的**某一**頂點，再訪問與此頂點鄰接且未被訪尋的頂點，當無法繼續向下訪問時，退回至最近被訪問的頂點，若其還有鄰接頂點未被訪尋過，則從該點繼續上述過程，直至訪尋完所有頂點。
#### 解法
DFS的實作則需要使用**堆疊(stack)**的資料結構，同時也需記錄頂點的狀態。假設*v1*為起始頂點，將*v1*放入stack，訪尋*v1*後，將*v1*從stack中刪除，並根據鄰接表將*v1*的鄰接點依序加入stack，同樣放入的鄰接點之狀態需為1，故將*v2*和*v5*加入stack。依據stack後進先出的原則，下一個訪尋的頂點為*v5*，同理，將*v5*從stack中移除，並將其鄰接點*v6*放入stack。以此類推，直至stack為空，則完成DFS走訪。
#### 圖示
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week12%2613/dfs.jpg">


















## Reference
1.https://www.bookofproofs.org/branches/examples-of-adjacency-matrices/<br>
2.http://wayne.cif.takming.edu.tw/datastru/graphs.pdf<br>
