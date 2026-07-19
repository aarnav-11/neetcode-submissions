# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        node = 0
        def goodV(root, maxV):
            nonlocal node
            if not root:
                return
            good = root.val >= maxV
            if good:
                node += 1
                maxV = root.val
            goodV(root.right, maxV)
            goodV(root.left, maxV)
        goodV(root, float("-inf"))
        return node
            
            