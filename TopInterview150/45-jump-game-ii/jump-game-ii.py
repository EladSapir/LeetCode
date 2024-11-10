class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        curr_end = 0
        farthest = 0
        jumps = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest

        return jumps