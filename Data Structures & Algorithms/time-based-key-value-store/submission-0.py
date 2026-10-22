class TimeMap:

    def __init__(self):
        self.pairs = {}
        self.values = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.pairs.get(key, [])
        values.append((timestamp, value))
        self.pairs[key] = values

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pairs:
            return ""
        values = self.pairs[key]
        if timestamp < values[0][0]:
            return ""
        left, right = 0, len(values)
        while left < right:
            mid = (left + right) // 2
            tstamp = values[mid][0]
            if tstamp > timestamp:
                right = mid
            else:
                left = mid + 1
        return values[left - 1][1] if left > 0 else ""