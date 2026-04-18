# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        small_dummy=ListNode()
        large_dummy=ListNode()
        small,large=small_dummy,large_dummy

        #counting for partioning
        count=0
        curr=head
        while curr:
            curr=curr.next
            count+=1
        
        if count%2==0:
            partition=count//2
        else:
            partition=count//2+1
        #partioning
        curr2=head
        count2=0
        while curr2:
            count2+=1
            if count2<=partition:
                small.next=curr2
                small=small.next
            else:
                large.next=curr2
                large=large.next
            curr2=curr2.next
        small.next=large.next=None

        #reversing the second half
        reverse=large_dummy.next
        prev=None
        while reverse:
            nxt=reverse.next
            reverse.next=prev
            prev=reverse
            reverse=nxt
        large_dummy.next=prev

        #merging them
        small_merge=small_dummy.next
        large_merge=large_dummy.next
        while large_merge:
            small_temp=small_merge.next
            large_temp=large_merge.next
            small_merge.next=large_merge
            large_merge.next=small_temp
            small_merge=small_temp
            large_merge=large_temp
        