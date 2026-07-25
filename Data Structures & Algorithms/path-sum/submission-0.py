# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def targetSumVal(root, currSum):
            if (not root):
                return False
            currSum += root.val
            if currSum == targetSum and not root.left and not root.right:
                return True
            if targetSumVal(root.left, currSum):
                return True
            if targetSumVal(root.right, currSum):
                return True
            currSum -= root.val
            return False
        return targetSumVal(root, 0)
            
