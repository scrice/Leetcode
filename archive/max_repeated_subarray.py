class Solution:
    def findLength(self, nums1, nums2):
        lengths = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i]==nums2[j]:
                    lengths[i][j] = lengths[i+1][j+1]+1
                print(i,j)
        return max(max(row) for row in lengths)




if __name__ == '__main__':
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    soln = Solution()
    result = soln.findLength(nums1,nums2)
    print(result)
