class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Instantiate 
        k = len(nums)-1
        i = 0
        
        while (i<=k):
            if nums[k] == val: #keep the value deleted
                    k-=1
            elif nums[i] == val:  # swap to end if value detected
                t = nums[k]
                nums[k] = nums[i]
                nums[i] = t
                k-=1
                i+=1
            else:   # otherwise move on
                i+=1

        return k+1