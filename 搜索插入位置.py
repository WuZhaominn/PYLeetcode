class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #左闭右闭   while(left <= right)   middle =left +(right-left)//2   if nums[middle] > target:right =middle-1
        #elif nums[middle] <target:left = middle+1     else:return middle
        
        
        #左闭右开   while(left < right)   middle =left +(right-left)//2   if nums[middle] > target:right =middle
        #elif nums[middle] <target:left = middle+1     else:return middle

        left,right = 0,len(nums)-1
        while left<=right:
            middle =left +(right-left)//2
            if nums[middle] < target:
                left = middle+1    # 范围缩小到 [mid+1, right]
            else:
                right =middle-1     # 范围缩小到 [left, mid-1]
        return left
