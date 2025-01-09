class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        dp=[0]*3
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            total=dp[1]+dp[2]
            dp[1]=dp[2]
            dp[2]=total
        return dp[2]
