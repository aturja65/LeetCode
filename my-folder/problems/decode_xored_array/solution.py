class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        ans.append(first)
        for number in encoded:
            first = number^first
            ans.append(first)
        return ans