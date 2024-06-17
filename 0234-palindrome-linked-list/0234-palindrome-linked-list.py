# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            if not fast.next.next:
                fast = fast.next
            else:
                fast = fast.next.next

        curr, nxt, prev = slow, None, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        rev = fast
        while head and rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
