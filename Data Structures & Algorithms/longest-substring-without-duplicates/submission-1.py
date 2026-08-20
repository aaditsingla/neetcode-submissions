class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest =0
        res =0
        
        ind=0
        i = 0
        seen = set()
        while i<len(s):
            if s[i] not in seen:
                seen.add(s[i])
                longest=longest+1
                i=i+1
            else:
                
                ind=ind+1
                i=ind
                longest =0
                seen.clear()
            res = max(res,longest)
        return res
            



            