# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 19:35:11 2019

@author: Yidi
"""

from collections import defaultdict

class Graph():    
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)] for row in range(vertices)]
        self.graph_list = defaultdict(dict)
        self.vertices = set()

    
    def addEdge(self, u, v, w):
        self.graph_list[(u,v)] = w
        self.vertices.add(u)
        self.vertices.add(v)

    
    def Dijkstra(self, s):
        dis_dict = dict(zip([str(i) for i in range(self.V)], self.graph[s]))
        #print(dis_dict)
        add_vertex = [str(s)]
        
        while True:
            vertex = self.getKey(dis_dict, add_vertex)  
            #print(vertex)
            if vertex is False:
                break
          
            add_vertex.append(vertex)

            adj_vertices = [str(i) for i in range(self.V) if str(i) not in add_vertex and self.graph[int(vertex)][i] != 0]
            
            for i in adj_vertices:
                if dis_dict[i] == 0:
                    dis_dict[i] = dis_dict[vertex] + self.graph[int(vertex)][int(i)]
                else:
                    if dis_dict[vertex] + self.graph[int(vertex)][int(i)] < dis_dict[i]:
                        dis_dict[i] = dis_dict[vertex] + self.graph[int(vertex)][int(i)]
            #print(dis_dict)
        
        return dis_dict
  
    
    def getKey(self, dis_dict, add_vertex):   
        value = []
        for i in range(self.V):
            if str(i) not in add_vertex:
                value.append(dis_dict[str(i)])
       
        while 0 in value:
            value.remove(0)
        
        if value == []:
            return False
        
        for key in dis_dict.keys():     
            if dis_dict[key] == min(value):
                return key
 
           
    def Kruskal(self):
        edge_sort = sorted(self.graph_list.items(), key = lambda item: item[1])
        #print(edge_sort)
        disjoint_set = [[i] for i in self.vertices]
        
        result = []
        
        for edge in edge_sort:
            if self.findSet(disjoint_set, edge[0][0], edge[0][1]) is True:
                result.append(edge)
                disjoint_set = self.mergeSet(disjoint_set, edge[0][0], edge[0][1])
        
        edge_dict = {}
        for edge in result:
            key = str(edge[0][0]) + '-' + str(edge[0][1])
            edge_dict[key] = edge[1] 
 
        return edge_dict
                
    
    def findSet(self, disjoint_set, u, v):
        rep_u, rep_v = -1, -1
        
        for _set in disjoint_set:
            if u in _set:
                rep_u = _set[0]
        for _set in disjoint_set:
            if v in _set:
                rep_v = _set[0]
        #print(rep_u, rep_v)
        
        if rep_u == rep_v:
            return False
        else:
            return True

        
    def mergeSet(self, disjoint_set, u, v):
        set_u, set_v = [], []
        for _set in disjoint_set:
            if u in _set:
                set_u = _set
                disjoint_set.remove(_set)
                break
        for _set in disjoint_set:            
            if v in _set:
                set_v = _set
                disjoint_set.remove(_set)
                break
        set_u = set_u + set_v
        disjoint_set.append(set_u)
        #print(disjoint_set)
        return disjoint_set
        
        
 #Reference: 程式為理解概念後自行寫出，無參考資料       
