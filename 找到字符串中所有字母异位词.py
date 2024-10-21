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
            #如果s[right]在char_map中出现
            if char_map[ord(s[right])]>=1:
            #如果该字符在 p 中，将 count 减 1，表示少了一个待匹配字符       
                count -=1
            #将该字符的频率从 char_map 中减 1。无论该字符是否在 p 中，这一步都会减少它在 char_map 中的频率，以确保字符不被重复计算
            #如果字符 s[right] 是 p 中的字符：当 char_map[ord(s[right])] 的值大于等于 1 时，表示该字符在 p 中还需要匹配。减去 1 后，说明窗口已经匹配了这个字符一次。如果某个字符在窗口中重复出现（超过 p 中的需要次数），char_map[ord(s[right])] 的值会变成负数。通过这种机制，算法可以跟踪哪些字符出现了多于 p 中规定的次数
#如果字符 s[right] 不是 p 中的字符：如果该字符不在 p 中，char_map[ord(s[right])] 会被减成负数，因为初始化时该字符在 char_map 中的值为 0。减去 1 表示窗口包含了一个不需要的字符
            char_map[ord(s[right])] -=1
            right += 1
            if count == 0:
                res.append(left)
            #当窗口的大小达到p的长度时
            if right-left == len(p):
                #检查：当我们移除窗口最左边的字符 s[left] 时，该字符在 char_map 中的频率是否为非负值。说明该字符本来在 p 中是需要的，并且刚好匹配了。这时，移除它就会使得当前窗口的匹配数减少，因此需要把 count 加回 1，以表示还需要再匹配一个字符。
                if char_map[ord(s[left])]>=0:
                    count +=1
                #这一步将被移除的字符 s[left] 的频率加回到 char_map 中，恢复它在窗口外的频率。
                char_map[ord(s[left])] += 1
                left += 1
        return res
