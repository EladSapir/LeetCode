class Solution(object):
    def lengthOfLastWord(self, s):
        text = s.split()
        return len(text[-1])
        