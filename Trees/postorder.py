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

# it uses 2 stacks


def postorder_iterative_2(root):

    if (root == None):
        return
    stack_1, stack_2 = [], []
    stack_1.append(root)
    while(len(stack_1)):
        root = stack_1.pop()
        stack_2.append(root)
        if(root.left):
            stack_1.append(root.left)
        if(root.right):
            stack_1.append(root.right)
    while(len(stack_2)):
        root = stack_2.pop()
        print(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\npostorder traversal of binary tree is")
postorder_recursive(root)
print(f"\n\n")
print(postorder_iterative_2(root))
