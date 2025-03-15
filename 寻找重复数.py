class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_val =1
        max_val =len(nums)

        while min_val <max_val:
            mid = (max_val+min_val) //2

            count = sum(min_val <=num <= mid for num in nums)
#如果 count > mid - min_val + 1：表示在区间 [min_val, mid] 里存在重复元素；将右边界 max_val 缩小到 mid
#如果 count <= mid - min_val + 1：表示在区间 [mid + 1, max_val] 里可能存在重复元素，将左边界 min_val 增大到 mid + 1
            if count >mid-min_val +1:
                max_val =mid
            else:
                min_val =mid+1

        return min_val
