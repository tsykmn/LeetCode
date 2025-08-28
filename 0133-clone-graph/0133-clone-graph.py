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

        def dfs(tree):
            if tree in old_to_new:
                return old_to_new[tree]
            
            old_to_new[tree] = Node(tree.val)

            for neigh in tree.neighbors:
                old_to_new[tree].neighbors.append(clone(neigh))

            return old_to_new[tree]
        
        bfs_cloned = {node: Node(node.val)}
        queue = [node]

        def bfs(tree):
            while queue:
                cur = queue.pop(0)
                for neigh in cur.neighbors:
                    if neigh not in bfs_cloned:
                        bfs_cloned[neigh] = Node(neigh.val)
                        queue.append(neigh)
                    bfs_cloned[cur].neighbors.append(bfs_cloned[neigh])
            return bfs_cloned[tree]

        return bfs(node)
        