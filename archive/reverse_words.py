class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        output = []
        for word in words:
            output.append(word[::-1])
        return ' '.join(output)


        
if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    soln = Solution()
    result = soln.reverseWords(s)
    print(result)
