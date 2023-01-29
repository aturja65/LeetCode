class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        primeArr = [True]*n
        count, i = 0, 2
        while i * i <= n:
            for j in range(i+i,n,i):
                primeArr[j] = False
            i += 1
        for i in range(2,n):
            if primeArr[i]:
                count += 1
        return count