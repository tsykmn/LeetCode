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

        def reverse(lst):
            prev = None
            curr = lst
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        rev_lst = reverse(head)
        while head and rev_lst:
            if head.val != rev_lst.val:
                return False
            head = head.next
            rev_lst = rev_lst.next
        return True