# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # make numbers to string
        num1 = ''
        num2 = ''
        
        curr = l1
        while curr != None: 
            num1 += str(curr.val)
            curr = curr.next 
            
        curr = l2
        while curr != None: 
            num2 += str(curr.val)
            curr = curr.next 
        
        # add numbers together
        number = (str(int(num1[::-1]) + int(num2[::-1])))
        
        # do first iteration
        i = len(number)-1
        a = ListNode(number[i])
        answer = a
        
        # create linked list 
        i -=1
        while (i >=0):
            a.next = ListNode(number[i])
            a = a.next
            i-=1
        
        return answer
            
            
            
            
        
        