class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.data)

# To convert an inherently recursive procedures to iterative, we need an explicit stack


def postorder_iterative(root):

    if (root == None):
        return
    nodeStack = []
    nodeStack.append(root)
    while(len(nodeStack)):
        root = nodeStack.pop()
        if(root.right is not None):
            nodeStack.append(root.right)
            continue
        if(root.left is not None):
            nodeStack.append(root.left)
            continue
        print(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\npostorder traversal of binary tree is")
postorder_recursive(root)
print(f"\n\n\n")
print(postorder_iterative(root))
