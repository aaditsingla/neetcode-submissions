class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0] *(n+1)
        for i in range(n+1): 
            index = i
            for j in range(32):
                if i%2:
                    res[index] +=1
                i = i>> 1
            
        return res

                
        