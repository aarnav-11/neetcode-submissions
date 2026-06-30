# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid, reverse halfway and merge

        def find_mid(head):
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
        
        middle = find_mid(head)
        second_half = middle.next
        middle.next = None
        reversed_list = reverse_list(second_half)

        temp2 = reversed_list
        while reversed_list:
            temp = head.next
            head.next = temp2
            temp2 = reversed_list.next
            reversed_list.next = temp
            head = temp
            reversed_list = temp2




