class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, miss = 0, 0
        ans = dict(Counter(nums))
        for i in range(1, len(nums)+1):
            if ans.get(i) is None:
                miss = i
            elif ans[i] == 2:
                dup = i
        return [dup, miss]