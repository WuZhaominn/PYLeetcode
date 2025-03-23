class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right =0,len(nums)-2

        while left <=right:

            mid = left + (right-left)//2
            if nums[mid] <nums[-1]:
                right = mid-1
            elif nums[mid] >=nums[0]:
                left =mid+1
        return nums[left]
