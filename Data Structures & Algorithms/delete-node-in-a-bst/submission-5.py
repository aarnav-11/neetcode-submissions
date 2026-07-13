# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_min(root):
            while root and root.left:
                root = root.left
            return root

        def delete(root, val):
            if not root:
                return None
            if root.val > val:
                root.left = delete(root.left, val)
            elif root.val < val:
                root.right = delete(root.right, val)
            
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                min_root = find_min(root.right)
                root.val = min_root.val
                root.right = delete(root.right, min_root.val)
            return root
        return delete(root, key)


