# Definition for a binary tree node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        length = 0
        node = head
        while node!=None:
            length+=1
            node = node.next
        removal = length-n

        node = head
        if removal != 0:
            for i in range(removal-1):
                node = node.next
            node.next = node.next.next
        else:
            head = head.next

        return head



if __name__ == '__main__':
    head = [1,2,3,4,5]
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    n = 4
    soln = Solution()
    result = soln.removeNthFromEnd(head,n)
    print(result)


