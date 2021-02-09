from collections import deque
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfs_traversal_without_hierarchy(self, root: TreeNode):
        if not(root):
            return
        ans = []
        seen_nodes = set()
        q = Queue(0)
        q.put(root)
        while (q.qsize()):

            curr = q.get()
            if not(curr in seen_nodes):
                seen_nodes.add(curr)
                ans.append(curr.val)
            if curr.left is not None or curr.right is not None:
                if not(curr.left in seen_nodes):
                    q.put(curr.left)
                if not(curr.right in seen_nodes):
                    q.put(curr.right)

        return ans

# Runtime - O(n), Space - O(n)

    def bfs_traversal_recursive(self, root):
        ans = []
        if not root:
            return ans

        def helper_recursive(node, level):
            # start the current level
            if len(ans) == level:
                ans.append([])

            # append the current node value
            ans[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper_recursive(node.left, level + 1)
            if node.right:
                helper_recursive(node.right, level + 1)

        # starting the execution
        helper_recursive(root, 0)
        return ans

# Runtime - O(n), Space - O(n)

    def bfs_traversal_iterative(self, root):
        ans = []
        if not root:
            return ans

        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            ans.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                ans[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return ans


a = Solution()
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(13)
root.left.left = TreeNode(4)
root.left.right = TreeNode(15)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(1)
root.right.right.right = TreeNode(8)
# print(f"\n{a.bfs_traversal_without_hierarchy(root)}\n\n")
print(f"\n{a.bfs_traversal_recursive(root)}\n\n")
print(f"\n{a.bfs_traversal_iterative(root)}\n\n")
