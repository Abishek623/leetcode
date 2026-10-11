class Solution:
    def hammingWeight(self, n: int) -> int:
        u = 0
        while n:
            u += (n & 1)
            n >>= 1
        return u