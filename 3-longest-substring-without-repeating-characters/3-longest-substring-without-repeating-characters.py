class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # global max 
        gmax = 0
        # map letter -> boolean
        freq = {}
        # slide through window 
        i = 0
        for j in range(0, len(s)):
            # del repeat char
            if s[j] in freq:
                print ("del", s[i])
                while (s[i] != s[j]): 
                    del freq[s[i]]
                    i+=1
                del freq[s[i]]
                i+=1
            
            # add the next char 
            freq[s[j]] = True
            gmax = max(gmax, len(freq))
    
        return gmax
        
        
        
             
            
            
            