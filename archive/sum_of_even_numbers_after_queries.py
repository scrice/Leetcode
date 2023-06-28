class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        evensum = sum(num for num in nums if not num%2)
        result = [0]*len(nums)
        for i in range(len(nums)):
            output = nums[queries[i][1]]+queries[i][0]
            if nums[queries[i][1]]%2==0:
                evensum = evensum - nums[queries[i][1]]
            if output%2==0:
                evensum = evensum+output
            result[i] = evensum
            nums[queries[i][1]] = output
        return result
        
if __name__ == '__main__':
    nums = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    nums = [1]
    queries = [[4,0]]
    soln = Solution()
    result = soln.sumEvenAfterQueries(nums,queries)
    print(result)
