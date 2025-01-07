class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #递归  前序遍历
        # if not root:
        #     return None
        # root.right,root.left = root.left,root.right
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        #迭代 层序遍历（广度优先遍历）
        # if not root:
        #     return None
        # queue=collections.deque([root])
        # while queue:
        #     node = queue.popleft()
        #     node.left,node.right=node.right,node.left
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return root

        #迭代  前序遍历
        if not root:
            return None
        stack=[root]
        while stack:
            node=stack.pop()
            node.left, node.right = node.right, node.left                   
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
