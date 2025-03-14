class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        hash_size = n+1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] =0
        #标记数组中出现过的正整数，以便后续快速判断哪些正整数缺失
        for i in range(n):
            #得到当前元素的值
            if nums[i] % hash_size !=0:
                #计算出该值在数组中的位置
                pos = (nums[i] % hash_size) - 1
                #将位置 pos 的元素加上 hash_size 作为标记。先取余再加，防止数字过大
                nums[pos] = (nums[pos] % hash_size) + hash_size
        for i in range(n):
            if nums[i] <hash_size:
                return i+1
        return hash_size
