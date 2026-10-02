"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals) - 1):
            for j in range(i + 1, len(intervals)):
                if (min(intervals[i].end, intervals[j].end)
                    - max(intervals[i].start, intervals[j].start)) <= 0:
                    continue
                else:
                    return False
        return True