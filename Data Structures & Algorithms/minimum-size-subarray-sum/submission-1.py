from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        begin=0
        best_len=inf
        window_sum=0

        for end in range(len(nums)):
            window_sum+=nums[end]
            while window_sum>=target:
                window_len=end-begin+1
                if window_len < best_len:
                    best_len=window_len
                window_sum-=nums[begin]
                begin+=1
        if best_len==inf:
            return 0
        else:
            return best_len