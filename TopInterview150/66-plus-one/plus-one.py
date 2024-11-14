class Solution(object):
    def plusOne(self, digits):
        i=len(digits)-1
        while True:
            if digits[i] == 9:
                digits [i] = 0
                if i==0:
                    return [1] + digits
                i+=-1
            else:
                digits[i]+=1
                return digits

        