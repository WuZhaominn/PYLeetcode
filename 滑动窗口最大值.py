class Solution:#太难了，不懂啊
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #使用双端队列，
        if not nums or k == 0:
            return []
        n = len(nums)
        result = []
        dq = deque()  # 存储索引的双端队列

        for i in range(n):
            # 移除窗口外的元素（索引过期），当前索引 i 所对应的窗口范围为 [i - k + 1, i]，窗口大小为 k。
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            # 移除队列中所有比当前值小的元素，dq[-1] 代表队列的最右端元素。
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            # 添加当前元素索引
            dq.append(i)
            # 记录窗口的最大值（窗口大小达到 k 时）
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
