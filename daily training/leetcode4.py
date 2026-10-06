class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    
        for i in range(len(flowerbed)):
            if flowerbed[i] in flowerbed:
                return i

        return bool()



