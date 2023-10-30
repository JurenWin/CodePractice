class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sList = list(s)
        tList = list(t)
        try:
            for char in tList:
                print(char)
                sList.remove(char)
        except:
            #fails pop a char that doesnt exist
            return False
        if len(sList) > 0:
            return False
        return True