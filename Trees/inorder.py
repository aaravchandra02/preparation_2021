

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.data)
        inorder_recursive(root.right)


def inorder_iterative():
    pass


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\nInorder traversal of binary tree is")
inorder_recursive(root)
