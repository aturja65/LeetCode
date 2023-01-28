class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)+1):
            ans += [list(j)for j in combinations(nums, i)]
        return ans