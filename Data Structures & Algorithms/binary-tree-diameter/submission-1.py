# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_h = 0

        def dfs(root):
            nonlocal max_h
            if not root:
                return 0
            right = dfs(root.right)
            left = dfs(root.left)
            max_h = max(max_h, right + left)
            return 1 + max(right, left)
        dfs(root)
        return max_h
        
        