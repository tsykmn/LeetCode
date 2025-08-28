"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # recursive dfs

        if node is None:
            return None

        old_to_new = {}

        def clone(tree):
            if tree in old_to_new:
                return old_to_new[tree]
            
            old_to_new[tree] = Node(tree.val)

            for neigh in tree.neighbors:
                old_to_new[tree].neighbors.append(clone(neigh))

            return old_to_new[tree]
        
        return clone(node)
        