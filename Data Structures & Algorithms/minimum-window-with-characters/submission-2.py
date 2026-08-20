class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        needMap = {}
        window = {}

        for c in t:
            needMap[c] = needMap.get(c, 0) + 1

        have = 0
        need = len(needMap)

        res = [-1, -1]
        resLen = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in needMap and window[c] == needMap[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                leftChar = s[l]
                window[leftChar] -= 1

                if leftChar in needMap and window[leftChar] < needMap[leftChar]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""