class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        result = []
        start = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                result.append(str(nums[start]) if start == i - 1 else str(nums[start]) + "->" + str(nums[i - 1]))
                start = i

        # Handle the last range
        result.append(str(nums[start]) if start == len(nums) - 1 else str(nums[start]) + "->" + str(nums[-1]))

        return result