class Solution:
    def minPartitions(self, n: str) -> int:
        m=0
        for x in n:
            m = max(int(x), m)
        return m
        