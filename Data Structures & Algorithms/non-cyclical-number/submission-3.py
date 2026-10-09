class Solution:

    def getDigits(self, q: int) -> list:
        digits = []

        while q > 0:
            r = q % 10
            digits.append(r)
            q = q // 10

        return digits

    def isHappy(self, n: int) -> bool:
        
        seen = []
        while True:
            i = dsum = 0
            
            digits = self.getDigits(n)

            while i < len(digits):
                dsum += digits[i] ** 2
                i += 1
            
            if (dsum in seen):
                break
            elif (dsum == 1):
                return True
            else:
                seen.append(dsum)
                n = dsum

        
        return False