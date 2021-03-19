class Linked_list:
    #initialize linkedlist
    def __init__(self):
        self.head=None
        
    def print_list(self):
        temp=self.head
        llstring=" "
        #traverse through the linkedlist
        #here temp  refers to the node of the current list
        while(temp):
            llstring += str(temp.data) + "-->"
            temp=temp.next
        print(llstring)

    def insert_start(self,data):
        #as we insert at start we set the next of node as head
        node=Node(data,self.head)
        self.head=node
    
    def insert_end(self,data):
        if self.head==None:
            node = Node(data)
            self.head = node
            return 
        node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node
    
    def get_length(self):
        count=0
        temp = self.head
        while temp:
            count=count+1
            temp=temp.next
        return count
        
        
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Not a valid index")
        if index==0:
            self.head=self.head.next
            return 
        count = 0 
        temp = self.head
        while temp:
            if count == index-1:
                temp.next = temp.next.next
                break    
            
            temp=temp.next
            count=count+1
            
    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Not a valid index")
        
        if index==0:
            self.insert_start(data)
            return 
        count = 0 
        temp=self.head
        while temp:

            if count == index-1:
                node = Node(data,temp.next)
                temp.next=node
                return 
            count=count+1
            temp=temp.next
                
#class node to create a node
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


#create linkedlist
ll=Linked_list()
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)
ll.insert_start(1)
ll.print_list()
c=ll.get_length()
print(c)
ll.remove_at(2)
ll.print_list()
ll.insert_at(0,10)
ll.print_list()
ll.insert_at(2,12)
ll.print_list()