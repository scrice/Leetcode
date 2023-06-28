def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
#  2 3 4
#1 2 3 5
class Solution:
    def numDecodings(self,s):
        dp = [1, 0, 0]
        for c in s:
            dp_new = [0,0,0]
            dp_new[0]  = (c > '0') * dp[0] + dp[1] + (c <= '6') * dp[2]
            dp_new[1]  = (c == '1') * dp[0]
            dp_new[2]  = (c == '2') * dp[0]
            dp = dp_new
        return dp[0]


if __name__ == '__main__':
    s = "2101"
    soln = Solution()
    result = soln.numDecodings(s)
    print(result)
