class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first, fast = 0, 0
        while True:
            first, fast = nums[first], nums[nums[fast]]
            if first == fast:
                break
        second = 0
        while first != second:
            first, second = nums[first], nums[second]
        return first