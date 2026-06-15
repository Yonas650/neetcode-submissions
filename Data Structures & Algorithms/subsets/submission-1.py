class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(nums):
                res.append(path.copy())
                return
            #skip the value at the current index
            backtrack(i+1)

            #include the value at the current index
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
        backtrack(0)
        return res