# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        
        if(p.val < node.val and q.val < node.val):
            node = node.left
            return self.lowestCommonAncestor(node, p, q )
        elif p.val > node.val and q.val > node.val:
            node = node.right
            return self.lowestCommonAncestor(node, p, q)

        else: 
            return node
        