class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        nums.clear()
        for value in count.keys():
            nums.append(value)
        return len(nums)
        