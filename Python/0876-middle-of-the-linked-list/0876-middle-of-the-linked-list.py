# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow, fast = head, head

        while fast is not None:
            if fast.next is None:
                fast = fast.next
            else:
                fast = fast.next.next
                slow = slow.next
        return slow