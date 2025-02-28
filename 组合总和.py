class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtracking(candidates,target,0,0,[],res)
        return res
    
    def backtracking(self,candidates,target,total,index,path,res):
        if total == target:
            res.append(path[:])
            return         
        for i in range(index,len(candidates)):
            if total+candidates[i] > target:
                break
            total += candidates[i]
            path.append(candidates[i])

            self.backtracking(candidates,target,total,i,path,res)

            total -= candidates[i]
            path.pop()
