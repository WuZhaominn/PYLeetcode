class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        ls=len(nums)

        for i in range(ls-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=ls-1
            while j<k:
                curr=nums[i]+nums[j]+nums[k]
                if curr==0:
                    result.append([nums[i],nums[j],nums[k]])
                #去重处理
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif curr<0:
                    j+=1
                else:
                    k-=1
        return result
