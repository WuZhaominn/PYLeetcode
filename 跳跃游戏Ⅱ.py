class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        #cur_right: 当前跳跃范围的右端点，表示当前跳跃能覆盖的最右边位置（即“已建造的桥的右端点”）。
        #next_right: 下一座跳跃范围的右端点的最大值，表示在当前跳跃范围内能到达的最远位置（即“下一座桥的右端点的最大值”）。
        cur_right = 0
        next_right = 0
        for i in range(len(nums)-1):
            next_right = max(next_right,i+nums[i])
            if i ==cur_right:
                cur_right = next_right
                res +=1
        return res
