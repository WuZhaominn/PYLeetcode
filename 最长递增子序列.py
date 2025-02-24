class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)
        n=len(nums)
        dp = [1]*n
        res = 1
        for i in range (1,n):
            for j in range (0,i):
                if nums[i] >nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            res = max(dp[i],res)
        return res
