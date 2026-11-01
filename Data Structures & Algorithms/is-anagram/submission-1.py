class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        if len(s)!= len(t):
            return False

        for i in range(0,len(s)):
            if s[i] not in map1:
                map1[s[i]] = 1
            else:
                count = map1[s[i]]
                map1[s[i]] = count + 1
            if t[i] not in map2:
                map2[t[i]] = 1
            else:
                count = map2[t[i]]
                map2[t[i]] = count + 1

       
        return map1 == map2

        