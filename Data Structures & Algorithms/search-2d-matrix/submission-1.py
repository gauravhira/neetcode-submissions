class Solution:

    
    def binSearch(self, arr: List[int], target: int) -> bool:
        l = 0
        r = len(arr) - 1
        found = False

        while l <= r:

            m = (l + r) // 2
            if (arr[m] == target):
                found = True
                break
            elif (arr[m] < target):
                l = m + 1
            else:
                r = m - 1
        
        return found

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search

        for arr in matrix:
            res = self.binSearch(arr, target)

            if res:
                return True

        return False