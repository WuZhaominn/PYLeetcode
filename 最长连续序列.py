class Solution:chatgpt生成算法
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sort_nums=sorted(nums)
        max_length=1
        curr_length=1
        for i in range(1,len(sort_nums)):
            if sort_nums[i] == sort_nums[i-1]:
                continue
            elif sort_nums[i] == sort_nums[i-1] + 1:
                curr_length+=1
            else:
                max_length=max(max_length,curr_length)
                curr_length=1
        max_length=max(max_length,curr_length)
        return max_length
        
                


