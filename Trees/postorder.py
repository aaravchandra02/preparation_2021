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

# it uses 2 stacks - runtime = O(n), Space = O(n); where n = n. of nodes


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

# This uses only one stack - runtime = O(n), Space = O(h); where h is heiht of the tree


def postorder_iterative_1(root):
    s_1 = []
    curr = root
    while(curr != None or len(s_1) > 0):
        if(curr != None):
            s_1.append(curr)
            curr = curr.left
        else:
            temp = s_1[-1].right
            if (temp == None):
                temp = s_1.pop()
                print(temp.data)
                while(len(s_1) > 0 and temp == s_1[-1].right):
                    temp = s_1.pop()
                    print(temp.data)
            else:
                curr = temp


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\npostorder traversal of binary tree is")
postorder_recursive(root)
print(f"\n\n")
print(postorder_iterative_2(root))
print(f"\n\n")
print(postorder_iterative_1(root))
