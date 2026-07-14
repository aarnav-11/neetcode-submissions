# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        arr = []

        if not subRoot:
            return True
        if not root and subRoot:
            return False
        curr = root
        
        def search(root, val):
            if not root:
                return None
            
            search(root.left, val)
            if root.val == val:
                arr.append(root)
            search(root.right, val)

        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            
            return isSame(root1.right, root2.right) and isSame(root1.left, root2.left)
        
        search(root, subRoot.val)
        if len(arr) == 0:
            return False

        while arr:
            if isSame(arr[-1], subRoot):
                return True
            arr.pop()
        return False


