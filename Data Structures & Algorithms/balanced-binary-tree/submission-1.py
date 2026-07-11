# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            right = height(root.right)
            left = height(root.left)

            if abs(right - left) > 1:
                return -1
            
            if left == -1 or right == -1:
                return -1
            
            return 1 + max(left, right)

        if height(root) == -1:
            return False
        return True

            