class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans, i = len(nums), 0
        for num in nums:
            ans ^= num
            ans ^= i
            i += 1
        return ans