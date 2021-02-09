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


# root = TreeNode(1, 2, 2)
# root.left = TreeNode(2, 3, 3)
# root.right = TreeNode(2, 3, 3)
# print(f"\n{a.isSymmetric(root)}\n")
