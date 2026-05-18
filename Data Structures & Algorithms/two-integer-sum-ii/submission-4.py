class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, 1, 
        while i < len(numbers) - 1:
            total = numbers[i] + numbers[j] 
            if total == target:
                break
            if total < target and j + 1 < len(numbers):
                j += 1
            else:
                i += 1
                j = i + 1
        return [i + 1, j + 1]