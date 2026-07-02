# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        ret_val = dummy
        while dummy:
            minimum = float("inf")
            minptr = None
            i_store = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < minimum:
                    minimum = lists[i].val
                    minptr = lists[i]
                    i_store = i
            if i_store == -1:
                break
            lists[i_store] = lists[i_store].next
            dummy.next = minptr
            dummy = dummy.next
        return ret_val.next
            
        
            
            
