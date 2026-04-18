class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0 for _ in range(2*len(nums))]
        for i in range(len(ans)):
            if i<len(nums):
                ans[i]=nums[i]
            else:
                ans[i]=ans[i-len(nums)]
        return ans
