# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(tree):
            if not tree:
                return 0

            left = dfs(tree.left)
            right = dfs(tree.right)
            
            return max(left, right) + 1

        return dfs(root)