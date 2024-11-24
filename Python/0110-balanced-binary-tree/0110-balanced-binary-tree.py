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
        # height-balanced = depth never differs more than 1

        def dfs(tree):

            if not tree:
                return 0
            left = dfs(tree.left)
            right = dfs(tree.right)
            if (left==-1) or (right==-1):
                return -1
            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        height = dfs(root)
        return height != -1