# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #go till midpoint and then flip it.
        #compare flipped to actual

        def find_mid(head):
            fast, slow = head, head
            while fast.next and fast.next.next:
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
        
        midpoint = find_mid(head)
        second_half = midpoint.next
        midpoint.next = None

        reversed_second_half = reverse_list(second_half)

        while reversed_second_half:
            if head.val != reversed_second_half.val:
                return False
            head = head.next
            reversed_second_half = reversed_second_half.next
        return True
        