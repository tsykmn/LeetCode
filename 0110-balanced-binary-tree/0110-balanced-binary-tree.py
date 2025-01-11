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
        def dfs(root, num):
            if not root:
                return 0
            right = dfs(root.right, num+1)
            left = dfs(root.left, num+1)
            if right < 0 or left < 0 or abs(left-right) > 1:
                return -1
            return max(right, left) + 1
        return dfs(root, 1) >= 0