class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        # if tree is empty, new nose becomes root
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while True:
            # going left
            if value < current.value:
                if current.left is None:  # empty spot found
                    current.left = new_node
                    return
                current = current.left  # keep going left
            # going right
            else:
                if current.right is None:  # empty spot found
                    current.right = new_node
                    return
                current = current.right  # keep going right

    def search(self, value):
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
bst.insert(8)
bst.insert(4)
bst.insert(12)
bst.insert(2)
bst.insert(6)
bst.insert(10)
bst.insert(14)

bst.inorder(bst.root)
print(bst.search(6))
print(bst.search(99))
