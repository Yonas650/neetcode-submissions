class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path, res = [], []
        used= [False]*len(nums)

        def backtrack():
            if len(path)== len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True

                path.append(nums[i])
                backtrack()
                path.pop()
                used[i]=False
        backtrack()
        return res