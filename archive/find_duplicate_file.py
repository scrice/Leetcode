from collections import defaultdict
class Solution:
    def findDuplicate(self, paths):
        dic=defaultdict(lambda :[])
        for i in range(len(paths)):
            st=paths[i]
            lst=st.split(" ")
            for j in range(1,len(lst)):
                sp=lst[j].index("(")
                dic[lst[j][sp:]].append(lst[0]+"/"+lst[j][:sp])
        return [dic[i] for i in dic if len(dic[i])>1]
        
        

if __name__ == '__main__':
    paths1 = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    paths2 = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    soln = Solution()
    result = soln.findDuplicate(paths1)
    print(result)
