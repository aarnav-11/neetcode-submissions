# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #have one pointer move once and one move twice for each iteration
        #when the second pointer ends then return first

        slow, fast = head, head
        i = 1
        while fast:
            if i % 2 == 0:
                slow = slow.next
            fast = fast.next
            i += 1
        return slow
