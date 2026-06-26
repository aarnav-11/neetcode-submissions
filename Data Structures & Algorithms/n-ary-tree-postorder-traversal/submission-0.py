"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def post(node):
            if not node:
                return
            for i in range(len(node.children)):
                post(node.children[i])
            res.append(node.val)
        post(root)
        return res