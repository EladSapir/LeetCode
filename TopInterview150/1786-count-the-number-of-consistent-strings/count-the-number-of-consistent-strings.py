class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = len(words)
        for i in words:
            for j in i:
                if j not in allowed:
                    count -= 1
                    break

        return count