# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #check 1.val and 2.val
        #if 1.val <= 2.val then point curr.next to 1.val and make curr = curr.next
        #elif 2.val < 1.val then point curr.next to 2.val and make curr = curr.next
        #start curr with lesser head val
        dummy = node = ListNode()
        node.next = list1

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
        return node.next
        
