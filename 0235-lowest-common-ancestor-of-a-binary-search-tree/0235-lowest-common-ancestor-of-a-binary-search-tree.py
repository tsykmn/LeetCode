# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(tree):
            if not tree or tree == p or tree == q:
                return tree
            left = dfs(tree.left)
            right = dfs(tree.right)
            if left and right:
                return tree
            return left or right
        return dfs(root)
        