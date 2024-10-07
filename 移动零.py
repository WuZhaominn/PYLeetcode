class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ls=len(nums)
        point=0
        for i in range (ls):
            if nums[i]!=0:
                temp=nums[point]
                nums[point]=nums[i]
                nums[i]=temp
                point+=1
