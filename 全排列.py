class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #标记哪些元素使用过了
        res = []
        self.backtracking(nums,[],[False]*len(nums),res)
        return res

    def backtracking(self,nums,path,used,res):
        if len(path)  == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i]=True
            path.append(nums[i])
            self.backtracking(nums,path,used,res)
            path.pop()
            used[i]=False
