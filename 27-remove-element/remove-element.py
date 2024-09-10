class Solution(object):
    def removeElement(self, nums, val):
        counter = 0
        for i in nums:
            if i!=val:
                nums[counter]=i
                counter+=1

        return counter
        