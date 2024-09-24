列表 []
字典{}
元组()

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
        #try:如果 num 作为键已经存在于 hash 中，hash[num] 返回的是一个列表。使用 .append(index) 将当前索引 index 添加到该列表中。
        #except：当 num 作为键不在 hash中时，hash[num] = [index] 创建一个新条目，将 num 作为字典 hash的新键，并将索引 index 作为该键对应的列表的第一个元素。
        for index,num in enumerate(nums):
            try:
                hash[num].append(index)
            except KeyError:
                hash[num]=[index]
        #使用 hash查找 another 是否存在。如果 another 等于 num（即需要找到两个相同的数），检查 hash[another] 是否包含多个索引。如果有多个索引，返回这些索引；否则继续
        #如果 another 不等于 num，直接返回 num 的当前索引 index 和 another 对应的索引index1[0]（即 another 在数组中的索引）。
        #如果哈希表中没有 another，捕获 KeyError，并跳过该次迭代。
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

class Solution:哈希表2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        #一遍一遍循环，第一次哈希表为空，没有就会错误处理添加第一个数据，第二次循环如果第一个值是需要的就可以直接返回索引结束，如果没有就会添加第二个数据
        for index,num in enumerate(nums):
            another = target - num
            try:
                index1 = hash[another]
                return [index1,index]
            except KeyError:
                hash[num]=index
                
class Solution:#双指针
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = [(v,index) for index ,v in enumerate(nums)]
        nums_index.sort()
        #头尾指针
        begin,end=0,len(nums)-1
        while begin < end:
            curr = nums_index[begin][0]+nums_index[end][0]
            if curr==target:
                return [nums_index[begin][1],nums_index[end][1]]
            elif curr<target:
                begin +=1
            else:
                end -=1
