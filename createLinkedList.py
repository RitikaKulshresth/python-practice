class LinkedList:
    def __init__(self):
      self.head = None

        # starting from head
    def printList(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


list1=LinkedList()
n1=Node(10)
list1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3

list1.printList()
