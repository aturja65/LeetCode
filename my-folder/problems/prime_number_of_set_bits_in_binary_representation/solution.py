import math
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right+1):
            num = bin(i)
            if self.isPrime(num.count("1")):
                ans+=1
        return ans
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True