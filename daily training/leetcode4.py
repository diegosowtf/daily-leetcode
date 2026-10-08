class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        L = len(flowerbed)
        i = 0
        while i < L and n > 0:
            if flowerbed[i] == 1:
                i += 2          
            elif i == L - 1 or flowerbed[i + 1] == 0:
                n -= 1          
                i += 2          
            else:
                i += 3  




