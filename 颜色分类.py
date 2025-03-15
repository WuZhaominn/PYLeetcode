class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums,left,right):
            nums[left] ,nums[right] = nums[right],nums[left]
        #zero：指向下一个应该放置 0 的位置。初始值为 0。
        #two：指向下一个应该放置 2 的位置。初始值为数组长度，即 size。
        n =len(nums)
        if n<2:
            return
        zero = 0
        two = n
        i=0
        while i<two:
            if nums[i] == 0:
                swap(nums,i,zero)
                zero+=1
                i+=1
            elif nums[i] == 1:
                #直接跳过，1不参与排序
                i+=1
            else:
                two-=1
                swap(nums,two,i)
