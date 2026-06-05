##Binary Search Trees, is a tree where each node has a value and everything to the left is SMALLER and everything to the right is BIGGER
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)

        #if tree is empty, new nose becomes root
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while True:
            #going left 
            if value < current.value:
                if current.left is None: #empty spot found
                    current.left = new_node
                    return 
                current = current.left #keep going left
            #going right
            else:
                if current.right is None: #empty spot found
                    current.right = new_node
                    return
                current = current.right #keep going right
    
    def search(self,value):
        current = self.root
        while current: 
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False    
    
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(20)

bst.inorder(bst.root)          # 3 5 7 10 15 20 (sorted!)
print(bst.search(7))           # True
print(bst.search(99))          # False
