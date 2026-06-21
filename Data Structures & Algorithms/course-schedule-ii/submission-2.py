class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for pre, crs in prerequisites:
            prereq[pre].append(crs)
        out = []
        circle, visited = set(), set()
        def dfs(crs):
            if crs in circle:
                return False
            if crs in visited:
                return True
            
            circle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            circle.remove(crs)
            visited.add(crs)
            out.append(crs)

            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return out