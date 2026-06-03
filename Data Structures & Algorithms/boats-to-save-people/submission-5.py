import math

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        ans = 0
        l, r = 0, len(people) - 1

        while l < r:
            weight = people[l] + people[r]
            if weight <= limit:
                l += 1
            r -= 1
            ans += 1
        return ans if l !=r else ans + 1