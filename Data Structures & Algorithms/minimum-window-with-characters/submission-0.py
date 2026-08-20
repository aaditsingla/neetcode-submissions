class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        mymap = {}

        for i in t:
            mymap[i] = 1 + mymap.get(i, 0)

        tempmap = {}

        have = 0
        need = len(mymap)

        l = 0
        res = ""
        minlen = float("inf")

        for r in range(len(s)):
            # Add current right character to tempmap
            tempmap[s[r]] = 1 + tempmap.get(s[r], 0)

            # If this character is needed and its count is now satisfied
            if s[r] in mymap and tempmap[s[r]] == mymap[s[r]]:
                have += 1

            # While current window is valid, try to shrink it
            while have == need:
                windlen = r - l + 1

                if windlen < minlen:
                    minlen = windlen
                    res = s[l:r + 1]

                # Remove left character from window
                tempmap[s[l]] -= 1

                # If removing it makes the window invalid
                if s[l] in mymap and tempmap[s[l]] < mymap[s[l]]:
                    have -= 1

                l += 1

        return res