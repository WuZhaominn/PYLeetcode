class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def myBuildTree(pre_left,pre_right,in_left,in_right):
            #left：当前子树在中序遍历中的左边界。right：当前子树在中序遍历中的右边界。
            if pre_left >pre_right:
                return None
            #前序遍历中第一个节点就是根节点
            pre_root =pre_left
            #中序遍历中定位根节点
            in_root =index[preorder[pre_root]]
            #先把根节点建立出来
            root =TreeNode(preorder[pre_root])
            #得到左子树中的节点数目
            size_left_subtree = in_root-in_left
        #递归构造左子树，并连接到根节点
        #先序遍历中「从左边界+1 开始的size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到根节点定位-1」的元素
            root.left = myBuildTree(pre_left+1,pre_left+size_left_subtree,in_left,in_root-1)
        # 递归地构造右子树，并连接到根节点
        # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right =myBuildTree(pre_left+size_left_subtree+1,pre_right,in_root+1,in_right)
            return root
        n =len(preorder)
        index ={element:i for i,element in enumerate(inorder)}
        return myBuildTree(0,n-1,0,n-1)
