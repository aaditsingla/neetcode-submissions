class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i: i[0])
        
        res = [intervals[0]]

        for st, end in intervals:
            if res[-1][1]>= st:
                res[-1][1] = max(end,res[-1][1])
            else:
                res.append([st,end])
        
        return res
        