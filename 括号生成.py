class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item =='[':
                stack.append(']')
            elif item =='{':
                stack.append('}')
            #如果栈为空，表示右括号多了
            elif not stack or stack[-1] !=item:
                return False
            else:
                stack.pop()
        
        if not stack:
            return True
        #如果栈不为空，表示左括号多了
        else:
            return False
