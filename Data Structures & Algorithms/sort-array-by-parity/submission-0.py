class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pair, odd = [], []

        for num in nums:
            if num % 2 == 0:
                pair.append(num)
            else:
                odd.append(num)
        return pair + odd