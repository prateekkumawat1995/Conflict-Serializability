#!/usr/bin/env python
from collections import defaultdict
import sys 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
        print self.graph
 
    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in 
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be poped from 
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False	
file=open("/home/isea/Desktop/prateek/programlab/schedule","r")
s=file.readlines()
sno=0
x=0
for k in s:
	if int(k[1])>sno :
		sno=int(k[1])
g = Graph(sno)
for i in s:
	j=0
	while j<len(s):
			if j>x : 
				if ((s[j][2]==i[2] and s[j][1]!=i[1]) and (i[0]!='r' or s[j][0]!='r')) :
					g.addEdge(int(i[1]),int(s[j][1]))
			j=j+1		
	x=x+1				
if g.isCyclic() == 1:
    print "Graph has a cycle"
else:
    print "Graph has no cycle"
