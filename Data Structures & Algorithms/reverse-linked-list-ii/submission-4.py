# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        count=1
        prev,curr=None,head

        before_left=dummy
        for _ in range(left-1):
            before_left=before_left.next
            curr=curr.next
            count+=1
        l=before_left.next

        r=dummy
        for _ in range(right):
            r=r.next
        while count>=left and count<=right:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            count+=1
        
        l.next=curr
        before_left.next=r
        
        return dummy.next