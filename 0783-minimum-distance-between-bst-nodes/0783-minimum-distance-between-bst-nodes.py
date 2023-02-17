# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        #flatten tree into list
        
        
        def traverse(point, lst):
            
            if point:
                traverse(point.left, lst)
                lst.append(point.val)
                traverse(point.right, lst)
            return lst

        lst = sorted(traverse(root, []))
        
        #find diff
        
        
        return min([lst[i] - lst[i-1] for i in range(1, len(lst))])

        

        
        
