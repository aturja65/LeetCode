from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for count in counts.values():
            if count & 1 !=0:
                return False
        return True