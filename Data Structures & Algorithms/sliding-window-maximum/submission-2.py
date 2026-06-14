from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()

        queue.append(0)
        for i in range(len(nums)):
            if i - k + 1 > queue[0]:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans