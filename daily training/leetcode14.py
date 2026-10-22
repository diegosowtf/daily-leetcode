class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Suma de la primera ventana
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Deslizar la ventana una posición a la vez
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k