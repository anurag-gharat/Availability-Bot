class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        
        #no duplicate nodes allowed
        if data == self.data:
            return
        
        if data <self.data:
            #add data in left tree
            if self.left:
                self.left.add_child(data)
            else :
                self.left = BinarySearchTreeNode(data)
            
        else :
            #add data to right
            if self.right:
                self.right.add_child(data)
            else :
                self.right = BinarySearchTreeNode(data)
            
    def in_order_traversel(self):
        elements=[]
        
        #visit left tree first
        if self.left:
            #the calling function will return some list and add it to elements list
            elements += self.left.in_order_traversel()
        
        #visist base node
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversel()
            
        
        return elements
        
    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            #val might be n left sub tree
            if self.left:
                self.left.search(val)
                return True
            else :
                return False

        
        if val > self.data:
            # val might be in right
            if self.right:
                self.right.search(val)
                return True
            else :
                return False
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
        
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right=self.right.delete(val)
        
        else :
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val=self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)    
        
        return self
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__=="__main__":
    numbers=[4,2,6,1,5,8,9]
    numbers_tree=build_tree(numbers)
    print(    numbers_tree.in_order_traversel())
    print(numbers_tree.search(1))  
    numbers_tree.delete(1)
    print(    numbers_tree.in_order_traversel())        