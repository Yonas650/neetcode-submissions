class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i]= the number of distinct ways to reach stair i
        prev1=1
        prev2=1

        for _ in range(2,n+1):
            current=prev1+prev2
            prev1=prev2
            prev2=current
        return prev2