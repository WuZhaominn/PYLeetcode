class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0,len(nums)-1
        found =-1
        res =[-1,-1]
        while left <right:

            mid = left+(right-left) //2

            if nums[mid] ==target:
                found =mid
                break
            elif nums[mid] <target:
                left =mid+1
            else:
                right =mid -1
        if found ==-1:
            return [-1,-1]
        res=[found,found]
        for i in range(found+1,len(nums)):
            if nums[i] == target:
                res[1] =i
            else:
                break
        for j in range(found-1,-1,-1):
            if nums[j] ==target:
                res[0] =j
            else:
                break

        return res
