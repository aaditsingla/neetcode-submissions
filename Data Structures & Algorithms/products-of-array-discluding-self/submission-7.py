class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0 
        i=0
        prod = 1
        zerocount = 0
        res=[0]*len(nums)
        while count < 2:
            if count<1:
                if nums[i] !=0: 
                    prod=prod*nums[i]
                if nums[i] == 0:
                    zerocount += 1 
                    if zerocount ==1:
                        index = i
                
            
            else:
                if i == len(nums):
                    count +=1
                if zerocount>1:
                    return res
                if zerocount==1:
                    res[index] = prod
                    return res
                res[i]=prod//nums[i]
            i=i+1
            if i == len(nums):
                    i=0 
                    count +=1
        return res


