# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == [] or head == None:
            return False

        slow, fast = head, head.next

        while fast != slow:
            if fast == None or fast.next == None or fast.next.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        