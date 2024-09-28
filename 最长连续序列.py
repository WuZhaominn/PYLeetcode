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
        
            
class Solution:时间空间都为O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        max_len=0
        while num:
            n=num.pop()
            i=n+1
            l=0
            r=0
            while i in num:
                num.remove(i)
                i+=1
                r+=1
            i=n-1
            while i in num:
                num.remove(i)
                i-=1
                l+=1
            max_len=max(max_len,r+l+1)
        return max_len
