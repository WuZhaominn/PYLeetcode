class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -inf
        def dfs(node):
            #如果节点为空，直接返回 True，表示空树或到达叶子节点，符合 BST 条件。
            if not node:
                return True
            #递归遍历左子树
            if not dfs(node.left):
                return False
            nonlocal prev
            #检查当前节点值
            if node.val<=prev:
                return False
            #更新前一个节点值
            prev = node.val
            #递归遍历右子树
            return dfs(node.right)

        return dfs(root)
