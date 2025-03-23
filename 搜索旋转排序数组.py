class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n =len(nums)
        left,right = 0,n-1
        while left<=right:
            mid = left +(right-left)//2
        # 第一种情况：mid和target在不同的递增段
        # 如果mid在第二，target在第一,说明target在mid的左边
            if nums[mid] <=nums[n-1] <target:
                right = mid-1
        ## 如果mid在第一，target在第二，说明target在mid的右边
            elif target <=nums[n-1] <nums[mid]:
                left =mid +1
        # 第二种情况：mid和target在同一个递增段
            else:
                if target >nums[mid]:
                    left =mid+1
                else:
                    right =mid-1
        return left if nums[left] ==target   else -1
