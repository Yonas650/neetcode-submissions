# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
         dummy=ListNode(0,head)
         prev,curr=dummy,head

         while curr:
            for _ in range(m):
                if curr: 
                    prev=curr
                    curr=curr.next
    
            for _ in range(n):
                if curr: 
                    prev.next=curr.next
                    curr=curr.next
         return dummy.next