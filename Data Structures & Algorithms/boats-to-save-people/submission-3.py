class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        l, r, count = 0, len(people) - 1, 0
        people.sort()
        while l < r:
            if people[l] + people[r] > limit:
                count += 1
                people.pop(r)
                r -= 1
            elif people[l] + people[r] <= limit:
                count += 1
                people.pop(r)
                people.pop(l)
                r -= 2
        if len(people) == 1:
            return count + 1
        return count
