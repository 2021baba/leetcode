class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            digits = []
            while n > 0:
                digits.append(n%10)
                n=n//10
            
            if n in seen:
                return False
            seen.add(n)

            sum = 0
            for i in digits:
                sum = sum +i**2
            if sum ==n:
                break



                
        