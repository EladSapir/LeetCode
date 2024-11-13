class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        char_map = {}
        for c1, c2 in zip(s, t):
            if c1 in char_map:
                if char_map[c1] != c2:
                    return False
            else:
                if c2 in char_map.values():
                    return False
                char_map[c1] = c2
        return True