方法1：
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenth=len(nums)
        for i in range(lenth):
            for j in range(i+1,lenth):
                if nums[i]+nums[j]==target:
                    return [i,j]
方法2：哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for index,num in enumerate(nums):
            try:
                hash[num].append(index)
            except KeyError:
                hash[num]=[index]
        for index,num in enumerate(nums):
            another=target-num
            try:
                index1=hash[another]
                if another ==num:
                    if len(index1)>1:
                        return index1
                    else:
                        continue
                else:
                    return [index,index1[0]]
            except KeyError:
                pass   
