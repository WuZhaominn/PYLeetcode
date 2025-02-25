class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<=1:
            return s
        dp = [[False] *n for q in range (n) ]
        start = 0
        end = 0
        res = 0
        
        for i in range (n-1,-1,-1):
            for j in range (i,n):
                if s[i] == s[j]:
                    if j-i<=1 or dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j] and j-i+1>res:          
                    res = j-i+1
                    start = i
                    end = j
    
        return s[start:end+1]
