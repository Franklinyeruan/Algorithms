# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        
        # Sum until you get to a leaf node DFS then compare all of them 
        
        if root == None: return 0
        nodeHeight = {root: 1}
        
        h = 0
        
        def dfs(node, h):
            if node == None: return
            
            # if leaf node (base case)
            if node.left == None and node.right == None: 
                print("leaf!")
                h = max(h, nodeHeight[node])
                return h
        
            # add information about left node
            nodeHeight[node.left] = nodeHeight[node] + 1
            h1 = dfs(node.left, h)
            
            # add information about right node 
            nodeHeight[node.right] = nodeHeight[node] + 1
            h2 = dfs(node.right, h)
            
            if h1 == None: h1 = 0
            if h2 == None: h2 = 0
            return max(h1,h2)
        
        return dfs(root, h)
        