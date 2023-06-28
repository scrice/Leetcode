# Definition for a binary tree node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def findClosestElements(self, arr, k, x):
        scandex = 0
        entries = 0
        #find location to search around
        while arr[scandex]<x:
            scandex+=1
            if scandex>len(arr)-1:
                scandex-=1
                break

        frontdex = scandex
        backdex = scandex
        if arr[frontdex] == x:
            frontdex-=1
            backdex+=1
            entries+=1
        elif arr[frontdex]<x:
            backdex+=1
        else:
            frontdex-=1


        while entries < k:
            if backdex == len(arr):
                frontdex-=1
                entries+=1
            elif frontdex < 0:
                backdex+=1
                entries+=1
            elif ((abs(arr[frontdex]-x) < abs(arr[backdex]-x)) or (abs(arr[frontdex]-x) == abs(arr[backdex]-x) and arr[frontdex]<arr[backdex])):
                frontdex-=1
                entries+=1
            else:
                backdex+=1
                entries+=1
            
        return arr[frontdex+1:backdex]



if __name__ == '__main__':
    arr = [3,5,8,10]
    k = 2
    x = 15
    soln = Solution()
    result = soln.findClosestElements(arr,k,x)
    print(result)
