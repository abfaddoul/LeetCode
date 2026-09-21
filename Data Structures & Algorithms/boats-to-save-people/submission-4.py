class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        l, r, count = 0, len(people) - 1, 0
        people.sort()
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            count += 1
        return count