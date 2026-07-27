class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.append(target)
        idx = nums.index(target)
        return -1 if idx == len(nums) - 1 else idx