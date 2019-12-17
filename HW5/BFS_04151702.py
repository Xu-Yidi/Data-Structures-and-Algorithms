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
        
    def BFS(self, s):
        vertices = [i for i in self.graph if self.graph[i] != self.graph.default_factory()]
        status_dict = dict.fromkeys(vertices,1)
        #print(status_dict)
        
        queue = []
        result = []
        
        queue.append(s)
        status_dict[s] = 2

        while set(list(status_dict.values())) != {3}:
            vertex = queue.pop(0)
            #print(vertex)
            result.append(vertex)
            status_dict[vertex] = 3
            
            adj_vertices = self.graph[vertex]
            for item in adj_vertices:
                if status_dict[item] == 1:
                    queue.append(item)
                    status_dict[item] = 2
            #print(queue)
                    
        return result
    
    def DFS(self, s):
        vertices = [i for i in self.graph if self.graph[i] != self.graph.default_factory()] 
        status_dict = dict.fromkeys(vertices,1) 
        #print(status_dict)
        
        stack = []
        result = []
        
        stack.append(s)
        status_dict[s] = 2

        while set(list(status_dict.values())) != {3}:
            vertex = stack.pop()
            #print(vertex)
            result.append(vertex)
            status_dict[vertex] = 3
            
            adj_vertices = self.graph[vertex]
            for item in adj_vertices:
                if status_dict[item] == 1:
                    stack.append(item)
                    status_dict[item] = 2
            #print(queue)
                    
        return result
