# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists,0,len(lists)-1)

    def divide(self,l,lef,rig):
        if lef>rig:
            return None
        if lef == rig: 
            return l[lef]
        
        mid = (lef+rig)//2
        left = self.divide(l,lef,mid)
        right = self.divide(l,mid+1,rig)

        return self.conquer(left, right)


    def conquer(self, ll,rr):
        dummy = ListNode(0)
        curr= dummy

        while ll and rr:
            if ll.val <= rr.val:
                curr.next = ll
                ll = ll.next

            else:
                curr.next = rr
                rr = rr.next

            curr = curr.next

        if ll:
            curr.next = ll
        else:
            curr.next =rr

        return dummy.next


