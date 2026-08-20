class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestb=prices[0]
        maxp=0
        
        for tod in prices:
            maxp=max(maxp,tod-bestb)
            bestb=min(bestb,tod)

        return maxp
            
