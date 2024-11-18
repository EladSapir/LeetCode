# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        heads= [(root,root.val)]
        if root.val == targetSum and not root.left and not root.right:
            return True
        sons=[]
        while heads:
            for i,j in heads:
                if i.left:
                    sons.append((i.left,j+i.left.val))
                if i.right:
                    sons.append((i.right,j+i.right.val))
                if not i.right and not i.left:
                    if j == targetSum:
                        return True
            heads,sons=sons,[]
        return False
        