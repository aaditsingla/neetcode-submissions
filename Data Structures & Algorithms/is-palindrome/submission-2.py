class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        s=s.lower()
        count=0
        st=""
        for i in range(len(s)-1,-1,-1):
            k=ord(s[i])
            j=ord(s[count])
            if ((k-ord('a')) >= 0 and (k-ord('a')) <26) or (k-ord('0')>=0 and k-ord('0')<9):
                res=res+s[i]
            
            if ((j-ord('a')) >= 0 and (j-ord('a')) <26) or (j-ord('0')>=0 and j-ord('0')<9):
                st=st+s[count]
            count +=1

        if res == st:
            return True
        return False