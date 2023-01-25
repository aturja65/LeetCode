from itertools import combinations
class Solution:
    def sub_lists (self, nums):
        comb = []
        for i in range(len(nums)+1):
            comb += [list(j) for j in combinations(nums, i)]
        return comb
    def subsetXORSum(self, nums: List[int]) -> int:
        sub = self.sub_lists(nums)
        sum = 0
        for i in sub:
            if i==[]:
                continue
            mul = 0
            for j in i:
                mul ^= j
            sum += mul
        return sum