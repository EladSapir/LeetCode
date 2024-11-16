from collections import deque

class Solution(object):
    def isValid(self, s):
        check = []
        for i in s:
            if i in ['{','(','[']:
                check.append(i)
            if i == ')':
                if len(check)!=0 and check[-1]=='(':
                    check.pop(-1)
                else:
                    return False
            if i == ']':
                if len(check)!=0 and check[-1]=='[':
                    check.pop(-1)
                else:
                    return False
            if i == '}':
                if len(check)!=0 and check[-1]=='{':
                    check.pop(-1)
                else:
                    return False
        if len(check)==0:
            return True
        return False

        