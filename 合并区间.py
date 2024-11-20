class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:  # 处理空列表情况
            return []
        if len(intervals) == 1:  # 只有一个区间，无需合并
            return intervals
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] =max(merged[-1][-1],interval[1])
        return merged
