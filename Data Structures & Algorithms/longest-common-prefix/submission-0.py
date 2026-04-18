class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        min_len=len(min(strs, key=len))
        
        for i in range(min_len):
            count=0
            for j in range(1,len(strs)):
                if strs[0][i]== strs[j][i]:
                    count+=1
            if count==len(strs)-1:
                res+=strs[0][i]
            else:
                break
            
        return res
                    