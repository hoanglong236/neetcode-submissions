from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        if arr[-1] <= x:
            return arr[-k:]

        nums = [abs(num - x) for num in arr]
        closest = len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                closest = i - 1
                break

        ans = deque()
        l, r = closest, closest + 1
        for _ in range(k):
            if l < 0:
                ans.append(arr[r])
                r += 1
            elif r > len(nums) - 1:
                ans.append(arr[l])
                l -= 1
            elif nums[l] <= nums[r]:
                ans.appendleft(arr[l])
                l -= 1
            else:
                ans.append(arr[r])
                r += 1
        return list(ans)