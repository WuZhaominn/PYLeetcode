class Solution:
    def decodeString(self, s: str) -> str:
        
        def backtracking(s,i):
            res,multi = "",0
            while i<len(s):
                if '0' <= s[i] <='9':
                    multi =multi *10  +int(s[i])
                elif s[i] == '[':
                    i,tmp = backtracking(s,i+1)
                    res +=multi *tmp
                    multi = 0
                elif s[i] ==']':
                    return i,res
                else:
                    res +=s[i]
                i +=1
            return res   
        return   backtracking(s,0)
        
