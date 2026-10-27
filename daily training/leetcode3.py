class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximo = max(candies)
        return [c + extraCandies >= maximo for c in candies]

#[2,3,5,1,3], 3 inpput
#[true,true,true,false,true] output