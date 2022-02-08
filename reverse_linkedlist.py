class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
      self.head = None
    

        # starting from head
    def insert_at_begining(self,data):
        tmp = self.head
        self.head=Node(data)
        self.head.next=tmp
    
    def reverse_linked_list(self,data,target):
        prev=None
        curr=Node

        while(curr!=None):
            next=curr.next

            curr.next=prev


            prev=curr
            curr=next
        
    def printlist(self):
        if self.head is None:
            print("Linked List is empty")
        
        llstr=''
        itr=self.head
        while (itr!=None):
                llstr+=str(itr.data)+'---->'
                itr=itr.next
        print(llstr)

ll=LinkedList()
# num=int(input())
n1 = Node(10)
ll.head = n1
ll.insert_at_begining(5)
ll.insert_at_begining(10)
ll.insert_at_begining(15)
ll.insert_at_begining(20)
ll.insert_at_begining(25)
ll.printlist()