class Solution:
    def getDigits(self, n: int) -> List[int]:
        q = n
        digits = []

        while q > 0:
            r = q % 10
            digits.append(r)
            q = q // 10
        
        return digits[::-1]

    def plusOne(self, digits: List[int]) -> List[int]:

        m = len(digits)
        i = m - 1
        n = digits[0] * (10 ** i)

        while i > 0:
            i -= 1
            n += digits[m - i - 1] * (10 ** i)

        return self.getDigits(n + 1)