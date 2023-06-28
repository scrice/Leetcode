import collections
class Solution:
    def minCost(self, colors, neededTime):
        res = max_cost = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                    max_cost = 0
            res += min(max_cost, neededTime[i])
            max_cost = max(max_cost, neededTime[i])
        return res




if __name__ == '__main__':
    colors = "aabaa"
    neededTime =  [1,2,3,4,1]
    soln = Solution()
    result = soln.minCost(colors,neededTime)
    print(result)
