# Graph
在介紹BFS與DFS的定義前，首先應對圖(Graph)的概念有所了解，故本文會首先說明資料結構中的圖形結構與其基本表達方式<br>

**Content**<br>
[Graphs](#Graphs)<br>
[Some Concepts](#Some-Concepts)<br>
[Data Structures for Graphs](#Data-Structures-for-Graphs)<br>


## Graphs(圖)
A **graph** *G = (V, E)* is simply a set *V* of **vertices**（點) and a collection *E* of pairs of vertices from *V*, called **edges**(邊). Thus, a graph is a way of represnting connections or relationships between pairs of objects from some set *V*<br>
### Undirected Graph(無向圖)
An edge *(u,v)* is said to be **directed** from *u* to *v* if the pair *(u,v)* is ordered, with *u* preceding *v*. If all the edges in a graph are undirected , then we say the graph is an **undirected graph**.
>ex: G<sub>1</sub><br>
>V(G<sub>1</sub>) = {1,2,3,4}<br>
>E(G<sub>1</sub>) = {(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)}<br>

### Directed Graph(有向圖)
An edge *(u,v)* is said to be **undirected** if the pair *(u,v)* is not ordered. If all the edges in a graph are undirected, then we say the graph is an **undirected graph**.
>ex: G<sub>2</sub><br>
>V(G<sub>2</sub>) = {a,b,c,d,e,f,g,h,k}<br>
>E(G<sub>1</sub>) = {<a,b>,<b,c>,<b,f>,<c,a>,<c,e>,<c,g>,<d,b>,<d,f>,<f,g>,<g,e>,<g,k>,<h,f>,<k,h>}<br>

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
### Adjacency Matrix(鄰接矩陣)
The **adjacency matrix** *A(G)* for a graph *G = (E, V)* with n vertices is a *n × n* matrix whose *A(i,j)* entry is 1 if the *i<sup>th</sup>* vertex and *j<sup>th</sup>* vertex are connected, and 0 if they are not. Note that matrix *A* is symmetric if graph *G* is undirected, as *A(i,j)* = *A(j,i)* for all pairs of *i* and *j*.

$$
A[i,j]=
\begin{cases}
1, & if (V_i,V_j)\in E(G),\\\\\\
0, & if (V_i,V_j)\notin E(G)
\end{cases}
$$

Ex:<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week12%2613/graph_1.png" width="75%" height="75%"><br>

$$
A(directed)=
\left[ \begin{matrix}
	0 & 1 & 0 & 0 & 1 \\\\\\
	0 & 0 & 1 & 0 & 1 \\\\\\
	1 & 0 & 0 & 1 & 0 \\\\\\
	0 & 0 & 1 & 0 & 0 \\\\\\
	1 & 0 & 0 & 0 & 0
\end{matrix}\right]
A(undirected) =
\left[ \begin{matrix}
	0 & 1 & 1 & 0 & 1 \\\\\\
	1 & 0 & 1 & 0 & 1 \\\\\\ 
	1 & 1 & 0 & 1 & 0 \\\\\\
	0 & 0 & 1 & 0 & 0 \\\\\\
	1 & 1 & 0 & 0 & 0
\end{matrix}\right]
$$

### Adjacency List(鄰接表)
The **adjacency list** structure groups the edges of a graph by storing them in smaller, secondary containers that are associated with each individual vertex.<br>
當頂點個數很多而邊數較少時，鄰接矩陣的儲存方式將造成儲存空間的浪費，而鄰接表使用數組與鏈結串列結合的方式，將頂點儲存在一維數組中，並將頂點的鄰接點儲存在鏈結串列中
>Ex: directed graph(cont.)<br>
>[1]→[2]→[5]<br>
>[2]→[5]→[3]<br>
>[3]→[1]→[4]<br>
>[4]→[3]<br>
>[5]→[1]
>Ex: undirected graph(cont.)<br>
>[1]→[2]→[3]→[5]<br>
>[2]→[1]→[3]→[5]<br>
>[3]→[1]→[2]→[4]<br>
>[4]→[3]<br>
>[5]→[1]→[2]<br>

### Incidence Matrix(關聯矩陣)
The (vertex-edge) **incidence matrix** *I(G)* of a grapg *G = (E, V)*, is a *n × m* matrix defined as follows. The rows and columns of *I(G)* are indexed by *V(G)* and *E(G)*, respectively. The *A(i,j)* entry of *I(G)* is 0 if vertex v<sub>i</sub> and and edge e<sub>j</sub> are not incident, and otherwise it is 1 or -1 according as e<sub>j</sub> originates or terminates at i, respectively.<br>

$$
I[i,j]=
\begin{cases}
1, & if \ v_i \ is \ the \ origin \ of \ e_j,\\\\\\
-1, & if \ v_i \ is \ the \ destination \ of \ e_j,\\\\\\
0, & if \ e_i \ and \ v_i \ are \ not \ destination
\end{cases}
$$

Ex.<br>
<img src="https://github.com/Xu-Yidi/fluteanzi/blob/master/week12%2613/graph_2.jpg">
$$
I(G)=
\left[ \begin{matrix}
    -1 & 1 & -1 & 0 & 0 & 0 \\\\\\
	1 & 0 & 0 & -1 & 0 & 0 \\\\\\ 
	0 & -1 & 0 & 0 & 1 & 0 \\\\\\
	0 & 0 & 1 & 0 & 0 & -1 \\\\\\
	0 & 0 & 0 & 1 & -1 & 1
\end{matrix}\right]
$$

## Reference
1.https://www.bookofproofs.org/branches/examples-of-adjacency-matrices/<br>
2.http://wayne.cif.takming.edu.tw/datastru/graphs.pdf<br>
