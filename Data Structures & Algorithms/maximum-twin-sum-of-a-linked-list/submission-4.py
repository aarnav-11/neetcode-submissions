# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #reverse list and have 2 pointers
        #then add l1.val and l2.val together and then compare to max, updating
        #return max_val
        list_val = []

        while head:
            list_val.append(head.val)
            head = head.next
        
        mid = len(list_val) // 2
        list_vall, list_valr = list_val[:mid], list_val[mid:]
        list_valr = list_valr[::-1]
        
        max_val = 0
        for i in range(len(list_vall)):
            max_val = max(max_val, list_vall[i] + list_valr[i])
        return max_val
            
