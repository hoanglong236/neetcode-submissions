import math

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if people[-1] + people[-2] <= limit:
            return math.ceil(len(people) / 2) 

        ans = 0
        l, r = 0, len(people) - 1
        while r > - 1 and people[r] == limit:
            r -= 1
            ans += 1

        while l < r:
            if people[l] + people[r] < limit:
                step = 0
                while l + step < r and people[l + step] + people[r] < limit:
                    step += 1
                if l + step == r:
                    ans += math.ceil((r - l + 1) / 2)
                    return ans
                else:
                    for i in range(step, 0, -1):
                        people[l + i] = people[l + i - 1]
                l += 1
                r -= 1
                ans += 1
            elif people[l] + people[r] > limit:
                ans += 1
                r -= 1
            if people[l] + people[r] == limit:
                ans += 1
                l += 1
                r -= 1
        if l == r:
            ans += 1
        return ans