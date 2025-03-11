class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = n * [0]
        #单调栈，储存索引
        st =[]
        for i in range(n-1,-1,-1):
            t = temperatures[i]
            #维护一个单调递减栈
            #如果当前栈顶元素对应的温度小于等于当前温度，弹出栈顶,(因为当前温度更高，栈顶对应的温度已无用)
            while st and t>=temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] =st[-1]-i

            st.append(i)

        return ans
