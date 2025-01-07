class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #迭代
        # if not root:
        #     return 0
        # defth = 0
        # #创建一个双端队列（deque）对象
        # queue=collections.deque()
        # queue.append(root)

        # while queue:
        #     defth+=1
        #     for i in range(len(queue)):
        #         node=queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return defth


        #递归  后序遍历
        return self.getHight(root)

    def getHight(self,node):
        if not node:
            return 0
        
        leftHight=self.getHight(node.left)
        rightHeight=self.getHight(node.right)
        height=1+max(leftHight,rightHeight)
        return height
