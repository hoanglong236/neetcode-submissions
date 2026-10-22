class TimeMap:

    def __init__(self):
        self.pairs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.pairs.get(key, [])
        values.append((timestamp, value))
        self.pairs[key] = values

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pairs:
            return ""
        values = self.pairs[key]
        if values[0][0] > timestamp:
            return ""
        left, right = 0, len(values)
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1
        return values[left - 1][1] if left > 0 else ""