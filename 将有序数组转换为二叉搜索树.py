class Solution:
    def tran(self,nums:list[int],left:int,right:int)->TreeNode:
        if left>right:
            return None
        mid = left + (right - left)//2
        root = TreeNode(nums[mid])
        root.left = self.tran(nums, left, mid - 1)
        root.right = self.tran(nums, mid + 1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.tran(nums, 0, len(nums) - 1)
        return root
