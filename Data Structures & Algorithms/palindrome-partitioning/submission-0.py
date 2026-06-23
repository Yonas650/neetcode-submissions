class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path, res = [], []

        def is_palindrome(word):
            return word==word[::-1]
        
        def backtrack(start):
            if start==len(s):
                res.append(path.copy())
                return
            
            for end in range(start+1, len(s)+1):
                piece=s[start:end]

                if not is_palindrome(piece):
                    continue
                path.append(piece)
                backtrack(end)
                path.pop()
        backtrack(0)
        return res