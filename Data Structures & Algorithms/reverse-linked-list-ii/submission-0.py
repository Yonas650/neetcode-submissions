# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr,count=head,0
        l=r=None
        while curr:
            count+=1
            if left == right: 
                return head
            if count==left:
                l=curr
            if count==right:
                r=curr
            curr=curr.next
        if l!=None and r!=None:
            prev,curr2=None, l
            after = r.next
            while curr2!=after:
                nxt=curr2.next
                curr2.next=prev
                prev=curr2
                curr2=nxt
            l.next=curr2
            before_left=dummy
            for _ in range(left-1):
                before_left=before_left.next
            before_left.next=r
            return dummy.next