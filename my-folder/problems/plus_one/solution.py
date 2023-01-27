class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for value in digits:
            num = (num * 10) + value
        num += 1
        num = str(num)
        ans = [int(i) for i in num]
        return ans