from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        nums = [abs(num - x) for num in arr]
        closest = len(arr) - 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                closest = i - 1
                break

        if closest == 0:
            return arr[:k]
        if closest == len(arr) - 1:
            return arr[-k:]

        ans = deque()
        l, r = closest, closest + 1
        for _ in range(k):
            if l >= 0 and nums[l] <= nums[r]:
                ans.appendleft(arr[l])
                l -= 1
            else:
                ans.append(arr[r])
                r += 1
        return list(ans)