#!/usr/bin/env python
from collections import defaultdict
import sys 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack, stack):
 
        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in 
        # recStack then graph is cyclic
        for neighbour in self.graph[v+1]:
            if visited[neighbour-1] == False:
                if self.isCyclicUtil(neighbour-1, visited, recStack, stack) == True:
                    return True
            elif recStack[neighbour-1] == True:
                return True
 
        # The node needs to be poped from 
        # recursion stack before function ends
        recStack[v] = False
        stack.insert(0,v+1)
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        stack = []
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack,stack) == True:
                    print "Graph is not conflict serializable"
                    return 1
        print "Graph is conflict serializable\n"
        print stack


# Read schedule from file
file=open("/home/isea/Desktop/prateek/programlab/schedule","r")

# Store schedule in list s 
s=file.readlines()
sno=0
x=0
# Count no of transection in schedule
for k in s:
	if int(k[1])>sno :
		sno=int(k[1])

# Create a Graph class object		
g = Graph(sno)


# Perform precedence graph algorithm and create graph
for i in s:
	j=0
	while j<len(s):
			if j>x : 
				if ((s[j][2]==i[2] and s[j][1]!=i[1]) and (i[0]!='r' or s[j][0]!='r')) :
					g.addEdge(int(i[1]),int(s[j][1]))
			j=j+1		
	x=x+1
	
# Check graph is cyclic or not. If not cyclic then print the order of the schedule	
					
g.isCyclic()


#end of file
