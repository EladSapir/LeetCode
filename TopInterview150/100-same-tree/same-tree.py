# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        return sameT(p,q)

def sameT(p,q):
    if p == None and q == None:
        return True
    if p and q and p.val==q.val:
        if sameT(p.right,q.right) and sameT(p.left,q.left):
            return True
    return False
        