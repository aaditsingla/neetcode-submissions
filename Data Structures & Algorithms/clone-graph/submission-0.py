"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            copy=Node(node.val)
            oldtonew[node]=copy
            for cur in node.neighbors:
                copy.neighbors.append(dfs(cur))
            return copy
            




        oldtonew = {}   
        if node:
            return dfs(node)
        else:
            return None
        