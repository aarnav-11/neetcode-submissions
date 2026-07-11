# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_min(root):
            curr = root
            while root and root.left:
                root = root.left
            return root
        
        def delete(root, val):
            if root is None:
                return None

            if val > root.val:
                root.right = delete(root.right, val)
            elif val < root.val:
                root.left = delete(root.left, val)
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    min_node = find_min(root.right)
                    root.val = min_node.val
                    root.right = delete(root.right, min_node.val)
            return root
        
        return delete(root, key)

