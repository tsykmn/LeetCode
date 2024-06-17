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
        # 2 pointers: slow (keep track of middle) and fast (goes to end node)
        slow, fast = head, head

        # move the pointers for slow and fast to reverse the half part of node
        while fast and fast.next:
            slow = slow.next
            if not fast.next.next:
                fast = fast.next
            else:
                fast = fast.next.next

        # reverse the nodes for the endpart
        curr, nxt, prev = slow, None, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # compare with the original list to see if valid palindrome
        rev = fast
        while head and rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
