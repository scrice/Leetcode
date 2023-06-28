class Solution:
    def numRollsToTarget(self, n, k, target):
        memo = {}
        def dp(d,target):
            if d == 0:
                return 0 if target >0 else 1
            if (d,target) in memo:
                return memo[(d,target)]
            to_return = 0
            for i in range(max(0,target-k,target)):
                to_return+=dp(d-1,i)
            memo[(d,target)] = to_return
            return to_return
        return dp(n,target) %(10**9+7)


if __name__ == '__main__':
    n = 1
    k = 6
    target = 3
    soln = Solution()
    result = soln.numRollsToTarget(n,k,target)
    print(result)
