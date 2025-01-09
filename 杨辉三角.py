class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #保存所有行
        dp=list()
        for i in range(numRows):
            row =list()
            for j in range (0,i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(dp[i-1][j] + dp[i-1][j-1])

            dp.append(row)
        return dp

        
