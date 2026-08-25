# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []

        curr = head
        while curr:
            arr.append(curr)
            curr=curr.next

        pos = len(arr)-n
        temp = arr[pos]
        if pos == 0:
            return head.next
        c = head
        prev = None
        while c:
            if temp == c:
                prev.next = c.next
                c.next = None
                return head
            prev = c
            c = c.next
            

        
