class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, 1
        while i < len(numbers) - 1:
            while numbers[i] + numbers[j] < target and j + 1 < len(numbers):
                j += 1
            if numbers[i] + numbers[j] == target:
                break
            i += 1
            j = i + 1
        return [i + 1, j + 1]