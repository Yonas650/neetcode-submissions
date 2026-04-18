class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l].lower()!=s[r].lower():
                return s[l+1:r+1]==s[r:l:-1] or s[l:r]==s[r-1:l-1:-1]
                
            l+=1
            r-=1
        return True