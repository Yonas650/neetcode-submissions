class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        best=[]
        wind=[]
        for end in range(len(nums)):
            wind.append(nums[end])
            if end>=k:
                wind.remove(nums[end-k])
            if end>=k-1:
                maxim=max(wind)
                best.append(maxim)
        return best