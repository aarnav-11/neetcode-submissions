# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret_val = []
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            miniList = []
            for _ in range(length):
                curr = q.popleft()
                miniList.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ret_val.append(miniList)
        return ret_val
                