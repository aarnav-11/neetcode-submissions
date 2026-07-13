# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def level(root):
            if not root:
                return None
            level(root.left)
            arr.append(root.val)
            level(root.right)
        level(root)
        return arr[k-1]