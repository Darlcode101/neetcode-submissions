class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #store a hash table for each string 
        #store frequency of letters 
        #compare, if equal return true 
        d = dict()
        d2 = dict()

        for n in s:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        for n in t:
            if n in d2:
                d2[n] += 1
            else:
                d2[n] = 1
        
        if d == d2:
            return True 
        else:
            return False