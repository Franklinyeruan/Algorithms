"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # Edge Cases
        if node == None: 
            return None
        
        if len(node.neighbors) == 0:
            return Node(1, [])
        
        
        #DFS Save to map value -> Neighbor
        valToNeigh = {}
        visited = {}
        
        # run DFS
        def dfs(node):
            # visit the node
            visited[node] = True
            
            # action
            
            if len(node.neighbors) == 0:
                return 
            
            
            neighNum = []
            for neighbor in node.neighbors: 
                neighNum.append(neighbor.val)
            
            # list of ints, which constitutes the node we're talking about
            valToNeigh[node.val] = neighNum
            
            # go to neighbors 
            neighbors = node.neighbors
            for neighbor in neighbors: 
                if neighbor not in visited:
                    dfs(neighbor)
            
            # finish traversal 
            return
        
        dfs(node)
        
        
        
        
        # Create a map of value -> fresh node (Create all the nodes)
        valueToNode = {}
        for value in valToNeigh: 
            valueToNode[value] = Node(value)
        
        
        # Connect all the edges
        for value in valueToNode: 
            node = valueToNode[value]
            neighVals = valToNeigh[value]
            node.neighbors=[]
            
            for neighVal in neighVals: 
                neighbor = valueToNode[neighVal]
                node.neighbors.append(neighbor)
        

        
        return valueToNode[1]
            
    
        