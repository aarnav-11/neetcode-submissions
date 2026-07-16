"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = deque()

        if not node:
            return None
        if not node.neighbors:
            return Node(node.val)
        
        cloned = {node : Node(node.val)}
        q.append(node)

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    q.append(neighbor)
                    cloned[neighbor] = Node(neighbor.val)
                cloned[curr].neighbors.append(cloned[neighbor])
        return cloned[node]
        
    