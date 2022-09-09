class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        # ways(n) = 
            #ways if we took 1 step before
            # ways if we took 2 step before
            # way1 + way2 = total way. 
            
        a = [1, 2]
        
        for i in range(2, n):
            nex = a[i-1] + a[i-2]
            a.append(nex)
            
        return a[n-1]
            
        
            
        