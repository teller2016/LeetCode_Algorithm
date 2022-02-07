# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    
    def dfs(self, node):
        if not node:
            return
        
        self.dfs(node.left)
        self.result.append(node.val)
        self.dfs(node.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result=[]
        self.dfs(root)
        return self.result
        
        