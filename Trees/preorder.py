class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_recursive(root):
    if root:
        print(root.data)
        preorder_recursive(root.left)
        preorder_recursive(root.right)

# This version has o(n) runtime and space complexity.
def preorder_iterative(root):
    if (root == None):
        return
    nodeStack = []
    nodeStack.append(root)
    while(len(nodeStack)):
        root = nodeStack.pop()
        print(root.data)
        if(root.right is not None):
            nodeStack.append(root.right)
        if(root.left is not None):
            nodeStack.append(root.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\npreorder traversal of binary tree is")
preorder_recursive(root)
print(f"\n\n\n")
print(preorder_iterative(root))
