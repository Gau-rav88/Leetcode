class Solution:
    def isAnagram(self, s,t):
        if len(s)!=len(t):
            return False
    
        d_s={}
        d_t={}

        for char in s:
            d_s[char]=d_s.get(char,0)+1
        
        for char in t:
            d_t[char]=d_t.get(char,0)+1
        
        for key in d_s:
            if d_s[key]!=d_t.get(key,0):
                return False
        return True