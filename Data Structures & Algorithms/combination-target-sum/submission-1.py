class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path, res = [], []

        def backtrack(start, remaining):
            if remaining==0:
                res.append(path.copy())
                return
            if remaining<0:
                return
            for i in range(start, len(nums)):
                x=nums[i]
                path.append(x)
                backtrack(i, remaining-x) #reuse is allowed
                path.pop()
        backtrack(0,target)
        return res