class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        len1 = len(ransomNote)
        len2 = len(magazine)
        if len2<len1:
            return False
        for i in range(len(ransomNote)):
            ind = magazine.find(ransomNote[i])
            if ind ==-1:
                return False
            magazine = magazine[:ind] + '0' + magazine[ind+1:]
        return True


        