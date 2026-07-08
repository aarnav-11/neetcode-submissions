# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid, reverse halfway and then start linking head to head

        def mid(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        
        middle = mid(head)
        second = middle.next
        middle.next = None
        mid_reversed = reverse(second)
        
        while head and mid_reversed:
            temp = head.next
            head.next = mid_reversed
            head = temp
            temp2 = mid_reversed.next
            mid_reversed.next = head
            mid_reversed = temp2
        
        # if head:
        #     mid_reversed.next = head
        # elif mid_reversed:
        #     head.next = mid_reversed





