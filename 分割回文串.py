class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s,0,[],res)
        return res

    def backtracking(self,s,start,path,res):
        if start == len(s):
            res.append(path[:])
            return

        for i in range(start+1,len(s)+1):
            t = s[start:i]

            if t == t[::-1]:
                path.append(t)
                self.backtracking(s,i,path,res)
                path.pop()
