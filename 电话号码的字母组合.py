class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # 数字到字母的映射
        dig_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        results = []
        self.backtracking(digits, dig_char, 0, result, results)
        return results

    def backtracking(self, digits, dig_char, index, result, results):
        if index == len(digits):
            # 将当前的字母组合（result）添加到结果列表 results 中
            a = "".join(result)
            results.append(a)
        else:
            # 获取当前数字对应的字母
            digit = digits[index]
            # 遍历当前数字对应的所有字母
            for i in dig_char[digit]:
                result.append(i)
                self.backtracking(digits, dig_char, index + 1, result, results)
                result.pop()
