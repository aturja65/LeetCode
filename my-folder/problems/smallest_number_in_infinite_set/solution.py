class SmallestInfiniteSet:

    def __init__(self):
        self.l=[value for value in range(1,1001)]

    def popSmallest(self) -> int:
        ans=self.l.pop(0)
        return ans

    def addBack(self, num: int) -> None:
        if num not in self.l:
            self.l.append(num)
            self.l.sort()


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)