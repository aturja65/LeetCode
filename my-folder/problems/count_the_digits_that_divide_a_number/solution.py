class Solution:
    def countDigits(self, num: int) -> int:
        ans, temp = 0, num
        while temp:
            if num % (temp%10) == 0:
                ans += 1
            temp //= 10
        return ans