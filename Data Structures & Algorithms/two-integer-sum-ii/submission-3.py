class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j, n = 0, 1, len(numbers)
        while i < n:
            total = numbers[i] + numbers[j] 
            if total == target:
                break
            if total > target:
                i += 1
                j = i + 1
            else:
                if j + 1 < len(numbers):
                    j += 1
                else:
                    i += 1
                    j = i + 1
        return [i + 1, j + 1]