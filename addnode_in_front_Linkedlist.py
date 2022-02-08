# 1) At the front of the linked list 
# 2) After a given node. 
# 3) At the end of the linked list

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
        

    def printlist(self):
        if self.head is None:
            print("Linked List is empty")
        
        llstr=''
        itr=self.head
        print(itr)
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
ll.printlist()

