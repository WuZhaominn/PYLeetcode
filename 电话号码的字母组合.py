class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        #数字到字母的映射
        dig_char ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }


        def backtracking(index):
            if index==len(digits):
            #将当前的字母组合（res1）添加到结果列表 res 中
                a="".join(result)
                results.append(a)
            else:
                #加入输入2，3，那第一轮的时候digit就为2
                digit = digits[index]
                #i在abc中
                for i in dig_char[digit]:
                    result.append(i)
                    backtracking(index+1)
                    result.pop()
        result = []
        results = []
        backtracking(0)
        return results
