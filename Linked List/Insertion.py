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

    #after a certain position
    def middle(self,position,data):
        k=1
        s=Node(data)
        temp=self.head
        while temp.next:
            if (k)==(position-1):
               s.next=temp.next
               temp.next=s
               break
            k+=1
            temp=temp.next

    #after a certain node
    def afternode(self,prev_node,data):
        if prev_node is None:
            print("error")
        s=Node(data)
        s.next=prev_node.next
        prev_node.next=s

    #at the end
    def last(self,data):
        s=Node(data)
        if self.head is None:
            self.head=s
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next=s


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

llist.middle(2,9)
llist.printList()

llist.afternode(llist.head.next,7)
llist.printList()

llist.last(40)
llist.printList()

--------------------------------------------------
3
1
2
3
3 2 1 
3 9 2 1 
3 9 7 2 1 
3 9 7 2 1 40
