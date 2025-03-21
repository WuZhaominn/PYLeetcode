class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last ={}

        for i,c in enumerate(s):
            last[c] =i  #更新字符 c 的最后出现下标
        ans = []
        start = end =0
        for i,c in enumerate(s):
            end = max(end,last[c])
            if end ==i:
                ans.append(end-start +1)
                start =i+1
        return ans
