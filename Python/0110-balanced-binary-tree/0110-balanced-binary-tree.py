# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(tree):
            if not tree:
                return 0
            
            right = dfs(tree.right)
            left = dfs(tree.left)

            if abs(right-left) > 1 or left < 0 or right < 0:
                return -1

            return max(right, left) + 1

        return dfs(root) >= 0