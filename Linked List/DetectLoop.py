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

    def loop(self):
        k=1
        temp1=self.head
        temp2=self.head
        while temp1 and temp2 and temp2.next  :
            temp1=temp1.next
            temp2=temp2.next.next

            if temp1==temp2:
                k=0
                print("loop")
                break

        if(k):
            print("no loop")




llist1=LinkedList()
print("linked list 1")
#keep n 4
#testing
n=int(input())
for i in range(n):
   k=int(input())
   llist1.last(k)

llist1.printList()
llist1.head.next.next.next.next = llist1.head

llist1.loop()

...........................................................................

linked list 1
4
1
2
3
4
o/p :
1 2 3 4 
loop
