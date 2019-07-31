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


    def duplicates(self):

        temp=self.head
        if temp is None:
            return
        while temp.next:
            if temp.data==temp.next.data:
                temp.next=temp.next.next
            else:
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
llist.duplicates()
llist.printList()


..................................................................

5
1
2
3
3
4
o/p :
4 3 3 2 1 
4 3 2 1
