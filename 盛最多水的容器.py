class Solution:
#自己写的暴力便利算法，超出时间限制
    def maxArea(self, height: List[int]) -> int:
        len1=len(height)
        a=[0]*(len1*(len1-1))
        k=0
        for i in range(len1):
            for j in range(i+1,len1):
                a[k]=min(height[i],height[j])*(j-i)
                k+=1
        return max(a)


class Solution:
#双指针
    def maxArea(self, height: List[int]) -> int:
        len1=len(height)
        left,right=0,len1-1
        if len1 < 2:
            return 2*min(height[left],height[right])
        curr_w,max_w=0,0
        while left<right:
            curr_w=min(height[left],height[right])*(right-left)
            max_w=max(curr_w,max_w)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_w
