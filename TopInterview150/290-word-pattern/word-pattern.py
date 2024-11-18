class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split(' ')
        biject = {}
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in biject.keys():
                if biject[pattern[i]]!=s[i]:
                    return False
            biject[pattern[i]]=s[i]

        if len(biject.values())==len(set(biject.values())):
            return True
        return False

        