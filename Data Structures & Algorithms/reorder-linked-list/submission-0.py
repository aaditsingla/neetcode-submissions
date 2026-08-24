# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr= head
        arr=[]
        count = 0
        while curr:
            arr.append(curr)
            curr=curr.next

        i,j= 0, len(arr)-1

        while i<j:
            arr[i].next = arr[j]

            i=i+1
            if i>=j:
                
                break
            arr[j].next = arr[i]
            j=j-1

        arr[i].next = None

        