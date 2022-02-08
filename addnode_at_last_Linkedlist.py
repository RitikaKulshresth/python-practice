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
    def insert_at_last(self,data):
        if self.head is None:
            self.head=Node(data,None)

        itr=self.head
        while(itr.next!=None):
            itr=itr.next
        itr.next = Node(data, None)  
        

    def printlist(self):
        if self.head is None:
            print("Linked List is empty")
        
        llstr=''
        itr=self.head
        # print(itr)
        while (itr!=None):
                llstr+=str(itr.data)+'---->'
                itr=itr.next
        print(llstr)

ll=LinkedList()
n1 = Node(10)
ll.head = n1
ll.insert_at_last(5)
ll.insert_at_last(10)
ll.insert_at_last(15)
ll.printlist()
