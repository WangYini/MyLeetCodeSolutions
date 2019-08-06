import sys
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        a = abs(x)
        temp = 0

        while a:
            pop = a % 10
            if temp * 10 > sys.maxsize or (temp * 10 == sys.maxsize and pop >7):
                return 0

            if temp * 10 < -sys.maxsize-1 or (temp * 10 == - sys.maxsize - 1 and pop > 8):
                return 0

            temp = temp * 10 + pop

            a = int(a / 10)
      

a = Solution()
print(a.reverse(1534236469))

