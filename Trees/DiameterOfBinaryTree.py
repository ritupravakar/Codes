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

    def diameter(self, s):

        if  s==-1:
            return 0

        else:
            lheight=self.height(self.graph[s][0])
            rheight = self.height(self.graph[s][1])
            ldiameter=self.diameter(self.graph[s][0])
            rdiameter=self.diameter(self.graph[s][1])

        return max(lheight+rheight+1,max(ldiameter,rdiameter))


n = int(input())
g = Graph(n)
for i in range(n):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    g.addEdge(i + 1, a)
    g.addEdge(i + 1, b)

print(g.diameter(1))

..............................................................
i/p:
5
2 3
4 5
-1 -1
-1 -1
-1 -1
o/p :
4
