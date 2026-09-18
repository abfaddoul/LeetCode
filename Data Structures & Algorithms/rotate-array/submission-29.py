class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        n = len(nums) - 1
        while i < k:
            temp = nums[n]
            nums.pop(n)
            nums.insert(0, temp)
            i += 1
