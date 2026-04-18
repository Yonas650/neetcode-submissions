class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        best=[]
        dq=deque()
        for end in range(len(nums)):
            while dq and nums[dq[-1]]<=nums[end]:
                dq.pop()
            dq.append(end)
            if dq[0]<=end-k:
                dq.popleft()
            if end>=k-1:
                best.append(nums[dq[0]])
        return best