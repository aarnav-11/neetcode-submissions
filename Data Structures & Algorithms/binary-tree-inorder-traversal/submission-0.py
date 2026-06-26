# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_order = []
        def inorderTraversal(node):
            if node is None:
                return
            

            inorderTraversal(node.left)
            in_order.append(node.val)
            inorderTraversal(node.right)
        inorderTraversal(root)
        return in_order