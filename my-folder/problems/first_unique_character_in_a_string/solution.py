class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = dict(Counter(s))
        for key in ans.keys():
            if ans[key]==1:
                return s.index(key)
        return -1