class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in numMap:
                return [numMap[x], i]
            numMap[nums[i]] = i # en cada iteracion se guarda como clave el valor de el i actual y se asigna i
            print(numMap)

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9)) 