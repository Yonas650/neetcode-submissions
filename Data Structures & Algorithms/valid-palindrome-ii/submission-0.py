class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l].lower()!=s[r].lower():
                if not s[l+1:r+1]==s[r:l:-1] and not s[l:r]==s[r-1:l-1:-1]:
                    return False
            l+=1
            r-=1
        return True