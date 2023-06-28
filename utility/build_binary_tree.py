# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to insert nodes in level order 
def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion 
    if i < n:
        root = TreeNode(arr[i]) 
  
        # insert left child 
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
  
        # insert right child 
        root.right = insertLevelOrder(arr, 2 * i + 2, n)
          
    return root
  
# Function to print tree nodes in 
# InOrder fashion 
def inOrder(root):
    if root != None:
        inOrder(root.left) 
        print(root.data,end=" ") 
        inOrder(root.right)