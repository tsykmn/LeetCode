# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # keep  track of nodes using levels
        # if same level, add the nodes in the list
        # continue searching on left and right with a level count
        # return the tracking

        nodes = []

        def dfs(tree, lvl):
            if not tree:
                return 
            
            if len(nodes) == lvl:
                nodes.append([])
            
            # nodes[lvl].append(tree.val)
            nodes[lvl].append(tree.val)
            dfs(tree.left, lvl+1)
            dfs(tree.right, lvl+1)

        dfs(root, 0)
        return nodes