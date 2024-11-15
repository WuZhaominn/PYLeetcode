class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #sum_map 用于存储每个累计和（curr_sum）的出现次数，初始时包含 {0: 1}。这样设置的目的是，当某个子数组的和恰好为 k 时，可以直接统计该情况。将 sum_map[0] 设置为 1，意味着累积和为 0 的情况在初始状态下已经出现了一次。
        sum_map = {}
        sum_map[0] = 1
        #count 用于统计满足条件的子数组数量。curr_sum 记录遍历数组时的累计和。
        count = curr_sum = 0
        for num in nums:
            curr_sum +=num
            # Check if sum - k in hash
            #curr_sum - k 的含义是：从当前位置往回看，是否存在一个累积和等于 curr_sum - k。如果 curr_sum - k 存在于 sum_map 中，说明在当前位置和前面的某一个位置之间的子数组和为 k。因此，将 sum_map[curr_sum - k] 的值加到 count 上（即累计和为 curr_sum - k 的出现次数），统计满足条件的子数组数量。
            count += sum_map.get(curr_sum - k ,0)
            # add curr_sum to hash
            sum_map[curr_sum] = sum_map.get(curr_sum,0) + 1
        return count
