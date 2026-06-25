class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = [-1, -1]
        start = 0
        distance, min_distance = 0, float('inf')
        for end in range(len(arr)):
            distance += abs(arr[end] - x)
            if end - start + 1 == k:
                if min_distance > distance:
                    min_distance = distance
                    ans = [start, end]
                distance -= abs(arr[start] - x)
                start += 1
        if min_distance == float('inf'):
            return arr
        return arr[ans[0]:ans[1] + 1]