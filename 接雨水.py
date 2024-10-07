class Solution:
    def trap(self, height: List[int]) -> int:
        ls=len(height)
        left,right=0,ls-1
        a,mle,mri=0,0,0
        while left<right:
            if height[left]<=height[right]:
                if height[left]>mle:
                    mle=height[left]
                else:
                    a+=mle-height[left]
                left+=1
            else:
                if height[right]>mri:
                    mri=height[right]
                else:
                    a+=mri-height[right]
                right-=1
        return a
