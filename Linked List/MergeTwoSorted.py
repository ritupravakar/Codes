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


def merge(head1, head2):
    temp=None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data<=head2.data:
        temp=head1
        temp.next=merge(head1.next,head2)
    else:
        temp=head2
        temp.next=merge(head1,head2.next)
    return temp



llist1=LinkedList()
print("linked list 1")
n=int(input())
for i in range(n):
   k=int(input())
   llist1.last(k)
llist1.printList()

llist2=LinkedList()
print("linked list 2")
n=int(input())
for i in range(n):
   k=int(input())
   llist2.last(k)
llist2.printList()

llist3=LinkedList()
llist3.printList()
llist3.head=merge(llist1.head,llist2.head)
llist3.printList()



.......................................................................

linked list 1
3
1
3
5
1 3 5 
linked list 2
3
2
4
6
2 4 6 
o/p :
1 2 3 4 5 6 
