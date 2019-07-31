class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

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

    def mid(self):
        temp1=self.head
        temp2=self.head
        while temp2 and temp2.next :
            temp1=temp1.next
            temp2=temp2.next.next
        print(temp1.data)




llist=LinkedList()
print("linked list 1")

n=int(input())
for i in range(n):
   k=int(input())
   llist.last(k)

llist.printList()
llist.mid()

........................................................................

linked list 1
5
1
2
3
4
5
o/p :
1 2 3 4 5 
3
