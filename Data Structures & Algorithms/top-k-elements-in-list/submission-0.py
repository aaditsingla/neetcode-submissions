class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums: 
            freq[i] = freq.get(i, 0) + 1
        fr = [[] for i in range(len(nums) + 1)]
        for n,f in freq.items():
            fr[f].append(n)
        result=[]
        for l in range(len(fr)-1,0,-1):
            for num in fr[l]:
                result.append(num)
                if len(result)==k:
                    return result




        