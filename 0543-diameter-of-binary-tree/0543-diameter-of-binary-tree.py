# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        d = [0]

        def diameter(tree, res):
            if not tree:
                return 0
            
            right = diameter(tree.right, res)
            left = diameter(tree.left, res)

            d[0] = max(d[0], right + left)

            return max(left, right) + 1
        
        diameter(root, d)
        return d[0]
        