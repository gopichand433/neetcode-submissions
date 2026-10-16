class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=[0]*len(nums)
        p=1
        z=0
        for i in nums:
        
            if i==0:
                z+=1
            else:
                p*=i
        if z>1:
            return pf
        elif z==1:
            for i in range(len(nums)):
                if nums[i] ==0:
                    pf[i]=p
                    return pf
        else:
            for i in range(len(nums)):
                pf[i]=p//nums[i]
        return pf
        
