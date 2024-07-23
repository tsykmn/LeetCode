# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        def dfs(tree, left):
            if not tree:
                return
            if not tree.right and not tree.left and left:
                self.total += tree.val
            dfs(tree.left, True)
            dfs(tree.right, False)
        dfs(root, False)
        return self.total