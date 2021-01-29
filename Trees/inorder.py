

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


def inorder_iterative(root):
    if root == None:
        return
    s = []
    while(True):
        if not(root == None):
            s.append(root)
            root = root.left
        else:
            if(len(s) == 0):
                break
            root = s.pop()
            print(root.data)
            root = root.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\n(Recursive)Inorder traversal of binary tree is:")
inorder_recursive(root)
print("\n(Iterative)Inorder traversal of binary tree is:")
inorder_iterative(root)
