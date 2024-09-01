class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            l, r = 0, len(self.timeMap[key]) - 1
            values = self.timeMap[key]
            while l <= r:
                mid = (l + r) // 2
                if values[mid][1] <= timestamp:
                    l = mid + 1
                else:
                    r = mid - 1
            return values[r][0] if r >= 0 else ""
        else:
            return ""
        
