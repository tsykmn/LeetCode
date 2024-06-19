# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pointers to traverse the lst
        slow = head
        fast = head
        while fast and fast.next:
            slow = head.next
            fast = fast.next.next
        return slow