class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitud = 0
        maxima = 0
        for g in gain:
            altitud += g
            maxima = max(maxima, altitud)
        return maxima
        