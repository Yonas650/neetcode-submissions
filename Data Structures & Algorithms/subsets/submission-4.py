class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(nums):
                res.append(path.copy())
                return
            #don't include the current element
            backtrack(i+1)

            #include the current element
            path.append(nums[i])
            backtrack(i+1)
            #undo the choice so other branches are clean
            path.pop()
        backtrack(0)
        return res