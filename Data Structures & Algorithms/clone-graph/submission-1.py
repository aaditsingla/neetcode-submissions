"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}
        if not node:
            return None
        q = deque([node])
        oldtonew[node]=Node(node.val)
    
        while q:
            Nd = q.popleft()
            for i in Nd.neighbors:
                if i not in oldtonew:
                    copy=Node(i.val)
                    oldtonew[i]=copy
                    q.append(i)
                oldtonew[Nd].neighbors.append(oldtonew[i])
                               
        return oldtonew[node]
            

          
       
        

       
        