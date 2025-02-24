class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0 or nums is None:
            return 0
        max_1= min_1=res=nums[0]
        for i in range(1,len(nums)):
            temp = max_1
            max_1 = max(nums[i],nums[i]*max_1,nums[i]*min_1)
            min_1 = min(nums[i],nums[i]*temp,nums[i]*min_1)
            res = max(max_1,res)
        return res
