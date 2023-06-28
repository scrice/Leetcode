# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root == None:
            return []
        else:
            left_side = self.inorderTraversal(root.left)
            right_side = self.inorderTraversal(root.right)
            return left_side+[root.val]+right_side

if __name__ == '__main__':
    # root = [3,1,4,3,null,1,5]
    # root = [1,0,1,0,0,0,1]
    # root = TreeNode(1,TreeNode(0,TreeNode(0),TreeNode(0)),TreeNode(1,TreeNode(0),TreeNode(1)))
    root = TreeNode(1,None,TreeNode(2,TreeNode(3)))
    soln = Solution()
    result = soln.inorderTraversal(root)
    print(result)


