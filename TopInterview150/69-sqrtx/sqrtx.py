
class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1

        return right