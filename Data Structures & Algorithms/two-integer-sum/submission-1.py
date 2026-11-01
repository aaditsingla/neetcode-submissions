class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #target = 7 
        #indices i != j 

        map1 = {}
        res= []

        for i in range(0, len(nums)):
            rem = target-nums[i]
            if rem in map1:
                res.append(map1[rem])
                res.append(i)
                return res
            if nums[i] not in map1:
                map1[nums[i]]=i
            
            

        
            
                



        