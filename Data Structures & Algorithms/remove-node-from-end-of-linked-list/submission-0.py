# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse_list(head):

            prev = None 
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        
        head = reverse_list(head)

        dummy = ListNode()
        dummy.next = head

        curr = dummy

        for _ in range(n - 1):
            curr = curr.next

        # remove curr.next
        curr.next = curr.next.next

        return reverse_list(dummy.next)
        
            


        
        