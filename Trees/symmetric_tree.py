# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
class TreeNode:
    # Utility function to create new node
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution_recursive:

    # Returns True if trees with roots as root1 and root2 are mirror
    def isMirror(self, root1, root2):
        # If both trees are empty, then they are mirror images
        if root1 is None and root2 is None:
            return True

        """ For two trees to be mirror images, the following three conditions must be true:
            1 - Their root node's data must be same
            2 - left subtree of left tree and right subtree of the right tree have to be mirror images
            3 - right subtree of left tree and left subtree of right tree have to be mirror images
        """
        if (root1 is not None and root2 is not None):
            if root1.data == root2.data:
                return (self.isMirror(root1.left, root2.right) and
                        self.isMirror(root1.right, root2.left))

        # If none of the above conditions is true then root1 and root2 are not mirror images
        return False

    def isSymmetric(self, root):

        # Check if tree is mirror of itself
        return self.isMirror(root, root)


# Driver Code
a = Solution_recursive()
# Let's construct the tree show in the above figure
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(f"\nSymmetric\n" if a.isSymmetric(
    root) == True else f"\nNot symmetric\n")


class Solution_iterative:
    # function to check if a given Binary Tree is symmetric or not
    def isSymmetric(self, root):

        # if tree is empty
        if (root == None):
            return True

        # If it is a single tree node, then it is a symmetric tree.
        if(not root.left and not root.right):
            return True

        q = []

        # Add root to queue two times so that it can be checked if either one child alone is NULL or not.
        q.append(root)
        q.append(root)

        # To store two nodes for checking their symmetry.
        leftNode = 0
        rightNode = 0

        while(not len(q)):

            # Remove first two nodes to check their symmetry.
            leftNode = q[0]
            q.pop(0)

            rightNode = q[0]
            q.pop(0)

            # if both left and right nodes exist, but have different values-. inequality, return False
            if(leftNode.data != rightNode.data):
                return False

            # append left child of left subtree node and right child of right subtree node in queue.
            if(leftNode.left and rightNode.right):
                q.append(leftNode.left)
                q.append(rightNode.right)

            # If only one child is present alone and other is NULL, then tree is not symmetric.
            elif (leftNode.left or rightNode.right):
                return False

            # append right child of left subtree node and left child of right subtree node in queue.
            if(leftNode.right and rightNode.left):
                q.append(leftNode.right)
                q.append(rightNode.left)

            # If only one child is present alone and other is NULL, then tree is not symmetric.
            elif(leftNode.right or rightNode.left):
                return False

        return True


# Driver Code
b = Solution_iterative()
# Let us construct the Tree shown in the above figure
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)
if (b.isSymmetric(root1)):
    print(f"\n\tThe given tree is Symmetric")
else:
    print(f"\n\tThe given tree is not Symmetric")

# root = TreeNode(1, 2, 2)
# root.left = TreeNode(2, 3, 3)
# root.right = TreeNode(2, 3, 3)
# print(f"\n{a.isSymmetric(root)}\n")
