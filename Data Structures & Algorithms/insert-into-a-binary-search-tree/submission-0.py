# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root

        def insert(root, val):
            curr = root
            if not root:
                return TreeNode(val)
            if root.val > val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
            return curr

        return insert(root, val)