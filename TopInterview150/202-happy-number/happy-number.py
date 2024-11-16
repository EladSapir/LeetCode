class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            num = 0
            while n>9:
                num +=(n%10)**2
                n=n//10
            n=num+n**2
        return True


        