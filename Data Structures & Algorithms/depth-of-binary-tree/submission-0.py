# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth_l, max_depth_r = 0, 0

        def maxd(node):
            if not node:
                return 0 
            max_dl = maxd(node.left)
            max_dr = maxd(node.right)

            return 1 + max(max_dl, max_dr)
            
        return maxd(root)