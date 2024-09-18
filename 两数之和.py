class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenth=len(nums)
        for i in range(lenth):
            for j in range(i+1,lenth):
                if nums[i]+nums[j]==target:
                    return [i,j]

