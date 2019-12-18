# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:49:35 2019

@author: Yidi
"""

from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    #def addEdge_1(self, u):
        #self.graph[u]
 
    def BFS(self, s):
        vertices = list(self.graph.keys())
        status_dict = dict.fromkeys(vertices,1) 
        
        queue = []
        result = []
        
        queue.append(s)
        status_dict[s] = 2

        while queue != []:
            vertex = queue.pop(0)
            result.append(vertex)
            status_dict[vertex] = 3
            
            adj_vertices = self.graph[vertex]
            for item in adj_vertices:
                if status_dict[item] == 1:
                    queue.append(item)
                    status_dict[item] = 2
                    
        return result
    
    def DFS(self, s):
        vertices = list(self.graph.keys())
        status_dict = dict.fromkeys(vertices,1) 
        
        stack = []
        result = []
        
        stack.append(s)
        status_dict[s] = 2

        while stack != []:
            vertex = stack.pop()
            result.append(vertex)
            status_dict[vertex] = 3
            
            adj_vertices = self.graph[vertex]
            for item in adj_vertices:
                if status_dict[item] == 1:
                    stack.append(item)
                    status_dict[item] = 2
                    
        return result
