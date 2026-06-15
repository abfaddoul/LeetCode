class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        cycle, visited = set(), set()
        out = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            out.append(crs)

            return True
        for crs in prereq:
            if dfs(crs) == False:
                return []
        return out