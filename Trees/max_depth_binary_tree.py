class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth_bottom_up_recursive(self, root):
        if root is None:
            return 0
        left_depth = self.max_depth_bottom_up_recursive(root.left)
        right_depth = self.max_depth_bottom_up_recursive(root.right)
        return max(left_depth, right_depth)+1

    # ans = 0

    # def max_depth_top_down_recursive(self, root, depth):
    #     if root is None:
    #         return 0
    #     if root.left is None and root.right is None:
    #         ans = max(ans,depth)
    #     self.max_depth_top_down_recursive(root.left, depth+1)
    #     self.max_depth_top_down_recursive(root.right, depth+1)


a = Solution()
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(13)
root.left.left = TreeNode(4)
root.left.right = TreeNode(15)
print(f"\n{a.max_depth_bottom_up_recursive(root)}\n\n")
print(f"{a.max_depth_top_down_recursive(root)}\n\n")
# print(f"{a.bfs_traversal_iterative(root)}\n\n")
