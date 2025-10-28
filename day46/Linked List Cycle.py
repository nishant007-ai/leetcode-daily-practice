class listnote (self,x):
    self.val = x 
    self.next = none 


class Solution :
    def has cycle(self,head):
    slow=head 
    fast = head 

    while slow and fast and fast.next :
        slow = slow.next 
        fast= fast.naxt.next 

        if slow == fast :
            return True
        else:
            return False
        
    def createlinkedlist (alues,pos):
        head = listnote (values[0])
        current = head 
        cycle_node = None 

        for index in range (1,len(values)):
            current.next = listnote (values[index])
            current = current.next 
            if index == pos:
                cycle_node = current 

        if pos != -1:
            current.next = cycle_node 

        return head