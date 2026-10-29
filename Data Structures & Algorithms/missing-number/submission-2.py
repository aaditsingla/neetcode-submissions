class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = len(nums)
        for i in range(n):
            xor ^= i ^ nums[i]

        return xor
            