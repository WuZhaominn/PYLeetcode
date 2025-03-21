class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #借助一个小顶堆来维护当前堆内元素的最小值，同时保证堆的大小为 k
        #遍历数组将元素入堆；如果当前堆内元素超过 k 了，我们就把堆顶元素去除，即去除当前的最小值
        #初始化小顶堆
        pq = []
        for num in nums:
            # 将当前元素加入堆,每次加入元素后，堆会自动调整为小顶堆（堆顶是最小元素）
            # Python 的 heapq 模块默认实现的是小顶堆
            heapq.heappush(pq,num)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]
