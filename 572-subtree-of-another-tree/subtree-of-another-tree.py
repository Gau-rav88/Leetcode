# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        if s is None and t is None:
            return True
        if t is None:
            return True
        if s is None and t is not None:
            return False
        return self.issame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        

    def issame(self,s,t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.issame(s.left,t.left) and self.issame(s.right,t.right)
    