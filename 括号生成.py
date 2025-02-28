class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtracking(n,[],0,0,res)
        return res

    def backtracking(self,n,path,left,right,res):
        if left==n and right==n:
            res.append("".join(path))
            return
        if left > n or right > n:
            return
        if left< right:
            return
        path.append("(")
        self.backtracking(n,path,left+1,right,res)
        path.pop()


        path.append(")")
        self.backtracking(n,path,left,right+1,res)
        path.pop()
        
