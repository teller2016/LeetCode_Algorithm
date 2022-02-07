# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, mini, maxi):
        if node is None:
            return True
        
        if node.val < mini or node.val > maxi:
            return False
        
        return self.dfs(node.left, mini, node.val-1) and self.dfs(node.right, node.val+1, maxi)
        
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini = float('-inf')
        maxi = float('inf')
        
        return self.dfs(root, mini, maxi)