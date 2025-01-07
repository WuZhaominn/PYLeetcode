# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #迭代  使用队列
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left) #将左子树头结点加入队列
        queue.append(root.right) #将右子树头结点加入队列
        #判断两个树是否互相翻转
        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            #左节点为空、右节点为空，此时说明是对称的
            if not leftNode and not rightNode: 
                continue
            #左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left) #加入左节点左孩子
            queue.append(rightNode.right) #加入右节点右孩子
            queue.append(leftNode.right) #加入左节点右孩子
            queue.append(rightNode.left) #加入右节点左孩子
        return True
            


    #     #递归   只能使用后序遍历
    #     if not root:
    #         return True
    #     return self.compare(root.left,root.right)

    # def compare(self,left,right):
    #     #首先排除空节点情况
    #     if left == None and right != None: 
    #         return False
    #     elif left != None and right == None: 
    #         return False
    #     elif left == None and right == None: 
    #         return True
    #     #排除了空节点，再排除数值不相同的情况
    #     elif left.val != right.val: return False
    #     outside = self.compare(left.left, right.right) #左子树：左、 右子树：右
    #     inside = self.compare(left.right, right.left) #左子树：右、 右子树：左
    #     isSame = outside and inside #左子树：中、 右子树：中 （逻辑处理）
    #     return isSame
