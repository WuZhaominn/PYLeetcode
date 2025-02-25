class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]
        dp = [[0]*n for q in range(m)]
        dp[0][0] =grid[0][0]

        for i in range (m):
            dp[i][0] = grid[i][0]+dp[i-1][0]
        if m>1 and n==1:
            return dp[m-1][0]

        for j in range (n):
            dp[0][j] = grid[0][j]+dp[0][j-1]
        if n>1 and m==1:
            return dp[0][n-1]
        for i in range (1,m):
            for j in range (1,n):
                dp[i][j] = min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
        return dp[m-1][n-1]
