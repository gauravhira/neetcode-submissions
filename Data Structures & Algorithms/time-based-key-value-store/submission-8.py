class TimeMap:

    def __init__(self):
        self.data = {} # {key: [value, timestamp]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (len(key) > 100 or len (key) < 1 or not key.isalnum() or not value.isalnum() or not key.islower() or not value.islower() or timestamp < 0 or timestamp > 10 ** 7):
            return
        if (key not in self.data):
            self.data[key] = []
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if (len(key) > 100 or len (key) < 1 or not key.isalnum() or not key.islower() or timestamp < 0 or timestamp > 10 ** 7):
            return
        res = ""
        values = self.data.get(key, [])
        l, r = 0, len(values) - 1
        
        while l <= r:
            m = (l + r) // 2
            if (values[m][1] <= timestamp):
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
            
        return res
