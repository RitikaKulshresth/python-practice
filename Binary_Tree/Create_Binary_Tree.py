
class TreeNode:
    def __init__(self,data=None,left=None,right=None):
            self.data=data
            self.left=None
            self.right=None


class Btree:
    def __init__(self,root):
      self.root = TreeNode(root)
    

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, [])
        elif traversal_type == "inorder":
            return self.inorderTraversal(tree.root, [])
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, [])

    
    def inorderTraversal(self,node,traversal):
        if not node:
            return []
        self.inorderTraversal(node.left, traversal)
        traversal.append(node.data)
        self.inorderTraversal(node.right, traversal)
        return traversal

tree=Btree(1)
tree.root.left=TreeNode(2)
tree.root.right=TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)
print(tree.print_tree("inorder"))










