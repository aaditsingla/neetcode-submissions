class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for c in range(1, len(dp)):
            for a in coins:
                if c-a >=0:
                    dp[c] = min(dp[c], 1 + dp[c-a]) 

        if dp[amount] != amount+1:
            return dp[amount]
        else:
            return -1
            