
class Solution(object):
    def mySqrt(self, x):
        i=0
        while True:
            if i*i == x:
                return i
            if i*i > x:
                return i-1
            i+=1
        