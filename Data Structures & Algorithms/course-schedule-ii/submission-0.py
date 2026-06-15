class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        output = []
        circle, visit = set(), set()
        def dfs(crs):
            if crs in circle:
                return False
            if crs in visit:
                return True
            
            circle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            circle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output