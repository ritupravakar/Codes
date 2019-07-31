class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    #beginning of the list
    def start(self,data):
        s=Node(data)
        s.next=self.head
        self.head=s


    def  nth(self,position):
        k=0
        temp=self.head
        while temp:
            if k==(position-1):
                print(temp.data)
                break
            k+=1
            temp=temp.next

    def printList(self):
        temp=self.head
        while temp :
            print(temp.data,end=" ")
            temp=temp.next
        print()
        
llist=LinkedList()
n=int(input())
for i in range(n):
   k=int(input())
   llist.start(k)
llist.printList()
llist.nth(3)

.......................................................................
4
1
2
3
4
o/p :
4 3 2 1 
2
