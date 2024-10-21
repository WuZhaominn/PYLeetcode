class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        char_map = [0] * 256
        for c in p:
            #ord(c)返回字符c的ASCII值，在值的位置加一
            char_map[ord(c)] += 1 
        #表示当前需要匹配的字符数量，初始状态下我们需要找到长度为 p 的异位词
        left,right,count = 0,0,len(p) 
        while right < len(s):
            if char_map[ord(s[right])]>=1:
                count -=1
            char_map[ord(s[right])] -=1
            right += 1
            if count == 0:
                res.append(left)
            if right-left == len(p):
                if char_map[ord(s[left])]>=0:
                    count +=1
                char_map[ord(s[left])] += 1
                left += 1
        return res
