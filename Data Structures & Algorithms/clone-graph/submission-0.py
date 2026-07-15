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
        if len(node.neighbors) == 0:
            return Node(1)

        adj_list = []
        q.append(node)
        clones = {node : Node(node.val)}

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                clones[curr].neighbors.append(clones[neighbor])
        return clones[node]
    