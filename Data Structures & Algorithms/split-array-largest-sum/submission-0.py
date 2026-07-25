class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefix = []
        running_sum = 0
        for num in nums:
            running_sum += num
            prefix.append(running_sum)
        
        left, right = 0, running_sum
        while left < right:
            mid = (left + right) // 2
            is_able = False
            tmp, i = k, 0
            while tmp > 0:
                cur_sum = 0
                while cur_sum + nums[i] <= mid:
                    cur_sum += nums[i]
                    i += 1
                    if i == len(nums):
                        break
                if i == len(nums):
                    is_able = True
                    break
                tmp -= 1
                print(cur_sum)
            print(mid, tmp, i, is_able)
            if is_able:
                right = mid
            else:
                left = mid + 1
        return left
                