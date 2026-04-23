class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = 0
        l = len(nums)
        ans = []
        while k < 2:
            i = 0
            while i < l:
                ans.append(nums[i])
                i += 1
            k +=1
        return ans           