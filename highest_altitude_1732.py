class Solution:
    def largestAltitude(self, gains):
        altitudes = [0]
        for i, gain in enumerate(gains):
            altitudes.append(altitudes[i]+gain)
        return max(altitudes)

if __name__ == '__main__':
    soln = Solution()
    gain = [-4,-3,-2,-1,4,3,2]
    result = soln.largestAltittude(gain)
    print(result)
