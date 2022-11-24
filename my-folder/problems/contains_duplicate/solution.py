class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for num in nums:
            if num not in ans:
                ans.add(num)
            else:
                return True
        return False