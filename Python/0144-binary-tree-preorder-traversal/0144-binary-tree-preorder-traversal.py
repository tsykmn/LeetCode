# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        def preOrder(tree):
            if not tree:
                return
            nodes.append(tree.val)
            preOrder(tree.left)
            preOrder(tree.right)
        preOrder(root)
        return nodes