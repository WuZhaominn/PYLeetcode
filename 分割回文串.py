class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s,0,0,[],res)
        return res
        # 参数:
        # - s: 输入字符串。
        # - i: 当前处理的字符索引。
        # - start: 当前回文子串的开始位置。
        # - n: 字符串的长度。
        # - path: 当前的回文子串分割路径。
        # - ans: 存储所有有效分割的结果集。
    def backtracking(self,s,start,i,path,res):
        if i == len(s):
            res.append(path[:])
            return
        #不选 i 和 i+1 之间的逗号（i=len(s)-1 时一定要选）
        #不选逗号： 继续处理下一个字符，不分割当前子串。
        if i < len(s)-1:
            self.backtracking(s,start,i+1,path,res)
        t = s[start:i+1]
        #选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
        #选逗号： 如果当前子串是回文，将其加入 path，并递归处理下一个子串。
        if t == t[::-1]:
            path.append(t)
            self.backtracking(s,i+1,i+1,path,res)
            path.pop()
