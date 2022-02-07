class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list= sorted(list(s))
        t_list= sorted(list(t))
        for a,b in list(zip(s_list,t_list)):
            if a!=b:
                return b
        
        return t_list[-1]