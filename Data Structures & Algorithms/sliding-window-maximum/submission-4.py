from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        ans = [0] * (len(nums) - k + 1)
        max_deque = deque()
        for i, num in enumerate(nums):
            while max_deque and max_deque[-1][1] <= num:
                max_deque.pop()
            max_deque.append((i, num))
            if i >= k - 1:
                while max_deque[0][0] < i - k + 1:
                    max_deque.popleft()
                ans[i - k + 1] = max_deque[0][1]
        return ans