class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        #dp[i] = number of ways to decode the first i characters
        dp = [0]*(n+1)

        #base case, one way to start decoding
        dp[0] = 1

        #the first digit is valid unless it's zero
        dp[1]=1 if s[0]!='0' else 0
        
        for i in range(2,n+1):
            #option1 final letter uses one letter
            if s[i-1]!='0':
                dp[i]+=dp[i-1]
            #option2 final letter uses two letters
            two_digits = int(s[i-2:i])
            if 10<=two_digits<=26:
                dp[i]+=dp[i-2]
        return dp[n]