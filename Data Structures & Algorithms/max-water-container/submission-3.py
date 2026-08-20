class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i=0
        size =0

        r = len(heights)-1
        while True:
            if r > i:
                s = abs(r-i)*min(heights[i],heights[r])
                if size < s:
                    size = s
            


            
            else:
                r = len(heights)
                i=i+1
            
            r=r-1

            if i == len(heights):
                break

        return size