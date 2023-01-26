class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            while num:
                temp.append(num%10)
                num //= 10
        return abs(sum(nums) - sum(temp))