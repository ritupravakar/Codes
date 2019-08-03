from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def topologicalSortUtil(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)

    def topologicalSort(self):
        visited=[False]*self.V
        stack=[]
        for i in range(self.V):
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        print(stack)



n = int(input())
g = Graph(n)
for i in range(n):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    g.addEdge(i , a)
    g.addEdge(i , b)
print(g.graph)
g.topologicalSort()

.......................................................................................

6
1 2
5 -1
3 -1
-1 4
-1 -1
-1 -1
defaultdict(<class 'list'>, {0: [1, 2], 1: [5, -1], 2: [3, -1], 3: [-1, 4], 4: [-1, -1], 5: [-1, -1]})
[0, 2, 3, 4, 1, 5]
