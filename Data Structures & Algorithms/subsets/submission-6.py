class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path, res = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(path.copy())
                return
            #don't include the current element
            backtrack(i+1)

            #include the current element
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
        backtrack(0)
        return res