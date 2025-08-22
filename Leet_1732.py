class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        final=[0]
        for i in gain:
            final.append(final[-1]+i)
        return max(final)
