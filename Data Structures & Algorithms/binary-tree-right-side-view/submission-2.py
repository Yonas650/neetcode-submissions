from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        if root:
            queue.append(root)
        res=[]
        while len(queue):
            level_size=len(queue)
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                last=level_size-1
                if i==last:
                    res.append(curr.val)
        return res