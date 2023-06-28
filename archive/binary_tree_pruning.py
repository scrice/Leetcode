# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self,root):
        if((not root.left) and (not root.right)):
            valid = root.val
            if(valid):
                return root
            else:
                return None
            #we have a 1
            
        if(root.left):
            root.left = self.dfs(root.left)
        if(root.right):
            root.right  = self.dfs(root.right)

        if((not root.left) and (not root.right)):
            if(root.val):
                return root
            else:
                return None
        return root

    def pruneTree(self, root: TreeNode) -> int:
        return self.dfs(root)

if __name__ == '__main__':
    # root = [3,1,4,3,null,1,5]
    # root = [1,0,1,0,0,0,1]
    root = TreeNode(1,TreeNode(0,TreeNode(0),TreeNode(0)),TreeNode(1,TreeNode(0),TreeNode(1)))
    soln = Solution()
    result = soln.pruneTree(root)
    print(result)

