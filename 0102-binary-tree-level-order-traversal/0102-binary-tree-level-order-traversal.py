# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # keep track of the nodes from each level
        levels = []
        def helper(node, lvl):
            if not node: # check if node empty
                return
            if len(levels) == lvl:
                levels.append([])
            
            helper(node.left, lvl+1)
            levels[lvl].append(node.val)
            helper(node.right, lvl+1)
            
        helper(root, 0)
        return levels