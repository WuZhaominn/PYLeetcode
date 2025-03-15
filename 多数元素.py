class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #votes 用于记录当前候选元素 x 的投票数
        votes = 0
        
        for num in nums:
            #当 votes 为 0 时：表示当前没有候选元素，或之前的候选元素已被抵消完毕。此时，将 num 设为新的候选元素 x
            if votes ==0:
                x=num
            if num ==x:

                votes +=1
            else:
                votes -=1
        return x
