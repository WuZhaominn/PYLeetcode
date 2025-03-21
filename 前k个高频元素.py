class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        #将频率和元素组成元组，存入列表
        heap =[(val,key) for key ,val in count.items()]
        # print(heap)
        #使用堆找到频率最高的 k 个元素,从堆中取出频率最大的 k 个元组
        top_k = heapq.nlargest(k,heap)
        # print("top-k",top_k)
        return [item[1] for item in top_k]
