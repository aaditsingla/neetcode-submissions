# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count = count +1
            curr = curr.next

        
        pos = count - n
        count =0
        if pos == 0:
            return head.next

        c = head
        while c:
            if count == pos:
                prev.next = c.next
                c.next = None
                return head
            count +=1
            prev = c
            c = c.next
            
            

        

        
