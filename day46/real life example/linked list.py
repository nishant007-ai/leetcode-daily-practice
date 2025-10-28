# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Helper function to create a linked list with a cycle
def createLinkedList(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node

    return head


# 🔍 Test Cases

