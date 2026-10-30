class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        premap = {i: [] for i in range(numCourses)}

        for crs, prq in prerequisites:
            premap[crs].append(prq)

        vis = set()

        def dfs(course):
            if course in vis:
                return False
            
            if premap[course] == []:
                return True
            vis.add(course)
            for i in premap[course]:
                if not dfs(i):
                    return False
            
            vis.remove(course)
            premap[course] = []
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        