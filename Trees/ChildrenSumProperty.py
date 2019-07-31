from collections import defaultdict
from collections import deque
import collections


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def height(self, s):
        if s==-1 :
            return 0
        return 1 + max(self.height(self.graph[s][0]), self.height(self.graph[s][1]))

    def isSum(self, s):

        l=0
        r=0
        if(s==-1 or(self.graph[s][0]==-1 and self.graph[s][1]==-1)):
            return 1
        else:
            if self.graph[s][0]!=-1:
                l=self.graph[s][0]
            if self.graph[s][1]!=-1:
                r=self.graph[s][1]
       # print(l)
       # print(r)
        if((s==l+r) and self.isSum(self.graph[s][0])and self.isSum(self.graph[s][1])):
            return 1

n = int(input())
g = Graph(n)
for i in range(n):

    r=int(input())
    if i==0:
        root=r
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    g.addEdge(r, a)
    g.addEdge(r, b)
#print(root)
#print(g.graph)
if(g.isSum(root)):
    print("Yes")
else:
    print("No")
    
-------------------------------------------------------------------------------------------
5
10
8 2
8
3 5
2
-1 -1
3 
-1 -1
5 
-1 -1
o/p :
Yes



