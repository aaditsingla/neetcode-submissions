class Solution:
    def findMin(self, nums: List[int]) -> int:
        j = 10000
        for i in nums:
            if i<j:
                j=i

        return j

        