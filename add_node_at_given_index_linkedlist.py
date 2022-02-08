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

    def get_length(self):
        count= 0
        itr=self.head
        while(itr!=None):
            count+=1
            itr=itr.next
        return count

    def insert_at_index(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception ("Invalid Index")

        if index==0:
            self.insert_at_begining()
        
        count=0
        itr=self.head
        while(itr!= None):
            count+=1
            if count == index-1:
                prev=itr.next
                temp=Node(data)
                itr.next=temp
                temp.next=prev
            itr=itr.next

    


    def insert_at_begining(self,data):
        tmp = self.head
        self.head=Node(data)
        self.head.next=tmp
        

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
ll.insert_at_begining(5)
ll.insert_at_begining(10)
ll.insert_at_begining(15)
ll.printlist()
ll.get_length()
ll.insert_at_index(3,6)
ll.printlist()