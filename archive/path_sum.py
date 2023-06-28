# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root,targetSum) -> int:
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

if __name__ == '__main__':
    # root = [3,1,4,3,null,1,5]
    # root = [1,0,1,0,0,0,1]
    root = TreeNode(1,TreeNode(0,TreeNode(0),TreeNode(0)),TreeNode(1,TreeNode(0),TreeNode(1)))
    soln = Solution()
    result = soln.pruneTree(root)
    print(result)

