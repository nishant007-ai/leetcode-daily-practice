class Solution:
    def addTwoNumbers(self, l1, l2):

        # Step 1: Create a dummy node
        dummy = ListNode(0)

        # Step 2: Pointer to build new linked list
        current = dummy

        # Step 3: Carry for addition
        carry = 0

        # Step 4: Loop until all digits and carry are finished
        while l1 or l2 or carry:

            # Step 5: Get values from l1 and l2
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            # Step 6: Add values and carry
            total = val1 + val2 + carry

            # Step 7: Update carry
            carry = total // 10

            # Step 8: Create new node with last digit
            current.next = ListNode(total % 10)

            # Step 9: Move current pointer
            current = current.next

            # Step 10: Move l1 and l2 forward
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Step 11: Return result (skip dummy node)
        return dummy.next
