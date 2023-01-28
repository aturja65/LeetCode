class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.helper(n,k)+1
    def helper(self, n, k):
        if n == 1:
            return 0
        return (self.helper(n-1, k)+k)%n