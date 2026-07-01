# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        len1, len2 = length(l1), length(l2)
        if len1 > len2:
            smaller = l2
            larger = l1
        else:
            smaller = l1
            larger = l2
        ret_val = larger

        while smaller:
            larger.val += smaller.val
            if larger.val >= 10:
                larger.val %= 10
                if larger.next:
                    larger.next.val += 1
                else:
                    larger.next = ListNode(1)
            larger = larger.next
            smaller = smaller.next

        while larger:
            if larger.val >= 10:
                larger.val %= 10
                if larger.next:
                    larger.next.val += 1
                else:
                    larger.next = ListNode(1)
            larger = larger.next

        return ret_val




    
