class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path, res= [], []
        candidates.sort()
        def backtrack(start, remaining):
            if remaining==0:
                res.append(path.copy())
                return
            if remaining<0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue

                x=candidates[i]
                path.append(x)
                backtrack(i+1, remaining-x)
                path.pop()
        
        backtrack(0, target)
        return res