class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #maxnum表示当前子数组以当前位置结束的最大和,numarr表示迄今为止找到的全局最大子数组和
        maxnum =maxarr= nums[0]
        #从第二个数字开始
        for i in range(1,len(nums)):
            maxnum = max(maxnum +nums[i],nums[i])
            maxarr = max(maxarr,maxnum)
        return maxarr
