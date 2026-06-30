# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #find midpoint
        #after midpoint, reverse list
        #compare reversed list to actual list so pointer post midpoint and pointer at start

        def midpoint(head):
            fast, slow = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse_list(head):
            prev = None

            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        
        midpoint = midpoint(head)
        reversed_s_half = reverse_list(midpoint)

        max_val = 0
        while reversed_s_half:
            max_val = max(reversed_s_half.val+head.val, max_val)
            reversed_s_half = reversed_s_half.next
            head = head.next
        
        return max_val


        
            
