class Solution:

    def encode(self, strs: List[str]) -> str:
        #first part 
        #run a loop of the list, encoding each string 
        res = ""
        for s in strs:
            res += str(len(s))+ "#" + s 
        return res 
            
        


    def decode(self, s: str) -> List[str]:
        #run a loop of the new list, decoding each string 
        res = []
        i = 0
        while i < len(s):
            # find the '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])       # number before '#'
            word = s[j+1:j+1+length]   # extract the string of that length
            res.append(word)
            i = j + 1 + length         # move pointer forward
        return res
