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

    def remove_at_begining(self):
        print(self.head)
        if self.head== None:
            raise Exception ('Nothing to remove')
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
            

    def remove_at_last(self):
        if self.head==None:
            raise Exception("Nothing to Delete")
        else:
            secondlast=self.head
            while(secondlast.next.next!=None):
                secondlast=secondlast.next
            secondlast.next=None
            
    def insert_at_last(self,data):
        if self.head is None:
            self.head=Node(data,None)

        itr=self.head
        while(itr.next!=None):
            itr=itr.next
        itr.next = Node(data, None)  

    def remove_at_index(self,index):
        if index < 0 or index > self.get_length():
            raise Exception ('Invalid Index')
        if index ==0:
            self.remove_at_begining()
        count=0
        itr=self.head
        while(itr!=None):
            count+=1
            if count == index-1:
                tmp=self.head.next
                self.head.next=self.head.next.next
                tmp=None
            itr=itr.next

    def find_middle_ele(self):
        fast_pointer=self.head
        slow_pointer = self.head
        while (fast_pointer.next != None and fast_pointer.next.next != None):
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        print("The middle element is -->",slow_pointer.data)


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
ll.insert_at_begining(2)
ll.insert_at_begining(15)
ll.insert_at_begining(17)
ll.printlist()
ll.get_length()
ll.find_middle_ele()
ll.printlist()
