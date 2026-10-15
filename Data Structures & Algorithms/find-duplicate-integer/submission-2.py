class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        second = 0
        while True:
            second = nums[second]
            slow = nums[slow]
            if second == slow:
                break
        return slow