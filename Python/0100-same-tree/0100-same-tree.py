# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # end of nodes
        if not p and not q:
            return True
        # if one tree has more nodes than the other; i.e. p or q not empty
        elif not p or not q:
            return False
        # not same nodes
        elif p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left) # continue to check left
        right = self.isSameTree(p.right, q.right)
        return left and right