class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)

        dp = [0]*(n+1) #dp[i] is the minimum cost required to reach stair i
        dp[0]=0
        dp[1]=0

        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]