class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 0
        sett = set(nums)
        for num in sett:
            if num-1 not in sett:
                length = 1
                while (num+length) in sett:
                    length +=1
                largest = max(length,largest)
        return largest
                
            