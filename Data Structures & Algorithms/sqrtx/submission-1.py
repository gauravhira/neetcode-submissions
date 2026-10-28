class Solution:
    def mySqrt(self, x: int) -> int:
        #   sqrt formula
        #   sqrt(n)  = I.G (Initial Guess) + [(n-[I.G x I.G]) / (2 * I.G)]
        
        from math import sqrt
        return (int(sqrt(x)))


        
        