# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        res = []
        heads=[root]
        sons=[]
        if root:
            res.append(root.val)
        while len(heads)!=0:
            for i in heads:
                if i.right:
                    sons.append(i.right)
                if i.left:
                    sons.append(i.left)
            avg = 0
            if len(sons)==0:
                break
            for i in sons:
                if i:
                    avg+=i.val
            res.append(float(avg)/len(sons))
            heads,sons = sons,[]

        return res




        