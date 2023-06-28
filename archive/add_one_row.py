# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(array):
    for element in array:
        print(element)

class Solution:
    def addOneRow(self, root, val, depth):
        if root == None:
            return None

        depth-=1
        if(depth==0):
            root.left = TreeNode(val,root.left,None)
            root.right = TreeNode(val,None,root.right)
            return root
        else:
            root.left = self.addOneRow(root.left,val,depth)
            root.right = self.addOneRow(root.right,val,depth)
            return root


if __name__ == '__main__':
    # root = [3,1,4,3,null,1,5]
    # root = [1,0,1,0,0,0,1]
    root = TreeNode(4,TreeNode(2,TreeNode(3),TreeNode(1)),TreeNode(6,TreeNode(5)))
    val = 1
    depth =1
    soln = Solution()
    result = soln.addOneRow(root,val,depth-1)
    print(result)


