class Solution:
    def add_two_numbers(self, n1, n2):

        dummy = ListNode(0)      # dummy node
        current = dummy          # pointer for result list
        carry = 0                # carry value

        while n1 or n2 or carry:

            # get value from first list
            if n1:
                k1 = n1.val
            else:
                k1 = 0

            # get value from second list
            if n2:
                k2 = n2.val
            else:
                k2 = 0

            # add values and carry
            total = k1 + k2 + carry

            # update carry
            carry = total // 10

            # create new node with last digit
            current.next = ListNode(total % 10)

            # move current pointer
            current = current.next

            # move input lists
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        return dummy.next
