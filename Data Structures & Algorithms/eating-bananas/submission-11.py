
import math

class Solution:
    def calcTime(self, arr: List[int], k: int) -> int:
        sumk = i = 0
        while i < len(arr):
            add = math.ceil(arr[i] / k)
            
            sumk += add
            i += 1
        
        return sumk

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        t = math.ceil(h / len(piles))
        mx = max(piles)
        total = sum(piles)
        start = math.ceil(mx / h)

        if (t == 1):
            return max(piles)
        elif (t < 1):
            return
        elif (total <= h):
            return 1

        # print ("start: ", start)
        # for i in range(start, mx):
        #     time = self.calcTime(piles, i)
        #     if (time <= h):
        #         k = i
        #         # print("found k at ", k)
        #         break
        #     # print("time, i = ", time, ", ", i)

        l = start
        r = mx

        while l <= r:
            m = (l + r) // 2
            time = self.calcTime(piles, m)
            if (time <= h):
                k = m
                # print("found k at ", k)
                r = m - 1
            else:
                l = m + 1

        return k

