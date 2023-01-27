class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = (n*(n+1))//2
        square = int(sqrt(sum))
        if square * square == sum:
            return square
        return -1