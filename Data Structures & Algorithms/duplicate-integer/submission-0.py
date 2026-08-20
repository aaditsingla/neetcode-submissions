class Solution:
    def hasDuplicate(self, nums: List[int]):
        dupl = set()
        for i in nums: 
            if i in dupl:
                return True
            dupl.add(i)
        return False 

