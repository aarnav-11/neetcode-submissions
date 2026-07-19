# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxH = 0
        
        def di(root):
            nonlocal maxH

            if not root:
                return 0
            left = di(root.left)
            right = di(root.right)
            maxH = max(maxH, left + right)
            return 1 + max(left, right)       

        di(root)
        return maxH