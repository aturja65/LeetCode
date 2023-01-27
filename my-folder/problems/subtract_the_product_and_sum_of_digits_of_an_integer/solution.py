class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, mul = 0, 1
        while n:
            sum += n%10
            mul *= n%10
            n //= 10
        return mul-sum