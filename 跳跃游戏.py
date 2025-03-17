class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #解题思路：尽可能到达最远位置（贪心）。如果能到达某个位置，那一定能到达它前面的所有位置。
        #记录最远能跳到哪里
        max_far = 0
        for idx,val in enumerate(nums[:-1]):
            max_far = max(max_far,idx+val)
            if max_far <=idx:
                return False
        return True
