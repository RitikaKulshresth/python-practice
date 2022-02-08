
class TreeNode:
    def __init__(self,data=None,left=None,right=None):
            self.data=data
            self.left=None
            self.right=None

class BStree:
    def __init__(self,rootData):
      self.root = TreeNode(rootData)
    
    def add_child(self,node,data):
        if not node:
            print("Root node is Empty")
            node=TreeNode(data)
            return self.root
        
        #if data is smaller than node node then add data in lef subtree
        if data <= node.data:
            if not node.left:
                node.left = TreeNode(data)
            else:
                self.add_child(node.left,data)
        #elif data is greater than node node then add data in right subtree
        elif data > node.data:
            if not node.right:
                node.right = TreeNode(data)
            else:
                self.add_child(node.right,data)

    
    def searchNode(self, node, target):
        if node.data==target:
            return True
        elif target<node.data:
            #val might be left subtree
            return self.searchNode(node.left,target)
        elif target<node.data:
            #val might be right subtree
            return self.searchNode(node.right,target)
        else:
            return False
     
    def in_order_traversal(self,node,traversal=[]):
        if not node:
            return []
        self.in_order_traversal(node.left)
        traversal.append(node.data)
        self.in_order_traversal(node.right)
        return traversal

    def pre_order_traversal(self,node,traversal=[]):
        if not node:
            return []
        traversal.append(node.data)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)
        return traversal

    def post_order_traversal(self,node,traversal=[]):
        if not node:
            return []
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        traversal.append(node.data)
        return traversal

    def size(self,node):
        if node == None:
            return 0
        ls=self.size(node.left)
        rs=self.size(node.right)
        ts = ls +rs + 1
        return ts

    def sum_node(self,node):
        if node == None:
            return 0
        lsm=self.sum_node(node.left)
        rsm=self.sum_node(node.right)
        tsm=lsm+rsm + node.data
        return tsm
    
    def max_node(self,node):
        if node == None:
            return 0
        lsm=self.max_node(node.left)
        rsm=self.max_node(node.right)
        tsm=max(node.data,(max(lsm,rsm)))
        return tsm

    def height(self, node):
        if node == None:
            return 0
        lh=self.height(node.left)
        rh=self.height(node.right)
        tsm=max(lh,rh)+1
        return tsm

    def level_order_traversal(self, node):
        nodeQueue=[node]
        to_list=[]

        while(len(nodeQueue)>0):
            node=nodeQueue.pop(0)
            to_list.append(node.data)
            if (node.left):
                nodeQueue.append(node.left)
            if (node.right):
                nodeQueue.append(node.right)
        return to_list

        ##TimeComplexity: O(N)
        #SpaceComplexity: O(N)

    def top_view_of_binary_Tree()

def build_tree(elements):
    tree=BStree(elements[0])
    for i in range(1,len(elements)):
        tree.add_child(tree.root,elements[i])
    return tree

if __name__=='__main__':
    numbers= [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree=build_tree(numbers)
    print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal(numbers_tree.root))
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal(numbers_tree.root))
    print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal(numbers_tree.root))
    print("Level Order Traversal",numbers_tree.level_order_traversal(numbers_tree.root))
    print("Search Node--->",numbers_tree.searchNode(numbers_tree.root, 99))
    print("Size of Binary Search Tree",numbers_tree.size(numbers_tree.root))
    print("Sum of Binary Search Tree",numbers_tree.sum_node(numbers_tree.root))
    print("Max of Binary Search Tree",numbers_tree.max_node(numbers_tree.root))
    

    

