class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        if target > nums[-1]:
            return end + 1
        if target < nums[0]:
            return 0
        while True:
            if target == nums[start]:
                return start
            if target == nums[end]:
                return end
            if end - start == 1 or end - start == 0:
                if target == nums[start]:
                    return start
                else:
                    return start + 1
            if target < nums[(start + end) // 2]:
                    end = (start + end) // 2
            else:
                    start = (start + end) // 2

        