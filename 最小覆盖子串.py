class Solution:#第一种方法，
    def minWindow(self, s: str, t: str) -> str:
        ls_s, ls_t = len(s), len(t)
        need_to_find = [0] * 256
        has_found = [0] * 256
        min_begin, min_end = 0, -1
        min_window = 100000000000000
        for index in range(ls_t):
            need_to_find[ord(t[index])] += 1
        count, begin = 0, 0
        for end in range(ls_s):
            end_index = ord(s[end])
            if need_to_find[end_index] == 0:
                continue
            has_found[end_index] += 1
            if has_found[end_index] <= need_to_find[end_index]:
                count += 1
            if count == ls_t:
                begin_index = ord(s[begin])
                while need_to_find[begin_index] == 0 or\
                    has_found[begin_index] > need_to_find[begin_index]:
                    if has_found[begin_index] > need_to_find[begin_index]:
                        has_found[begin_index] -= 1
                    begin += 1
                    begin_index = ord(s[begin])
                window_ls = end - begin + 1
                if window_ls < min_window:
                    min_begin = begin
                    min_end = end
                    min_window = window_ls
        # print min_begin, min_end
        if count == ls_t:
            return s[min_begin: min_end + 1]
        else:
            return ''



class Solution:#第二种方法出自GPT老师
    def minWindow(self, s: str, t: str) -> str:
        #使用两个字典：      need：记录 t 中每个字符的需求数量。     window：记录当前窗口中各字符的数量。
        need =Counter(t)
        print(need)
        window ={}
        left ,right =0,0
        #valid：记录当前窗口中满足字符需求的种类数。
        valid =0
        start,min_len =0,float('inf')
        while right < len(s):
            #扩展窗口
            char = s[right]
            right +=1

            #更新windows和valid
            if char in need:
                window[char] = window.get(char,0) + 1
                if window[char] ==need[char]:
                    valid += 1  



            #收缩窗口
            while valid ==len(need):
                #更新最小子串
                if right - left < min_len:
                    start =left
                    min_len = right -left
                
            #左指针收缩
                char = s[left]
                left +=1

            #更新windows和valid
                if char in need:
                    if window[char] == need[char]:
                        valid -=1
                    window[char] -=1
        return s[start:start+min_len] if min_len != float('inf') else ""
