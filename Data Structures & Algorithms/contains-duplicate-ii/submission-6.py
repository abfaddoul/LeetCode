class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hel = defaultdict(list)

        for i, num in enumerate(nums) :
            hel[num].append(i)

        for val in hel.values():
            for j in range(len(val) - 1):
                if val[j + 1] - val[j] <= k:
                    return True
        return False