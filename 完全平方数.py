class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化dp数组，dp[i]表示将数字i表示为完全平方数之和的最少个数
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 0需要0个完全平方数
        
        # 遍历每一个数字i
        for i in range(1, n + 1):
            # 检查所有可能的完全平方数
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]



