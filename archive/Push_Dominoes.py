class Solution:
    def pushDominoes(self, dominoes):
        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
            dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
            dominoes = dominoes.replace('.L', 'LL')         # <-- 2)

        return  dominoes.replace('xxx', 'R.L')              # <-- 3)




if __name__ == '__main__':
    dominoes = "RR.L"
    # dominoes = ".L.R...LR..L.."
    soln = Solution()
    result = soln.pushDominoes(dominoes)
    print(result)
