class listnote (slef,x):
    self.val=x
    self.next =None

class SOluti9on:
    def hash cyclyre (self ,head):
       slow = head
    fast = head
    while slow,fast and fast.next:
       slow = slow.next
       fast = fast.next .next

       if slow ==fast :
           return true 
     else :
        return false


    def createlinkedlsit(val,poes):
        head= listnote (val[0])
        current = head
        cycle_node = None           

        if index in range (1,len(val)):
            current.next = listnote (val[index])
            current = current.next
            if index == pos:
                cycle_node = current      