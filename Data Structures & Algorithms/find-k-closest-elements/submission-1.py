class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        nums = [0] * len(arr)
        nums[0] = abs(arr[0] - x)
        closest = len(arr) - 1
        set_closest = False
        for i in range(1, len(arr)):
            nums[i] = abs(arr[i] - x)
            if not set_closest and nums[i - 1] < nums[i]:
                closest = i - 1
                set_closest = True

        ans = []
        if closest == 0:
            return arr[:k]
        if closest == len(arr) - 1:
            return arr[-k:]

        l, r = closest, closest + 1
        print(nums, closest)
        for _ in range(k):
            if nums[l] <= nums[r]:
                ans.append(arr[l])
                l -= 1
            else:
                ans.append(arr[r])
                r += 1
        return sorted(ans)