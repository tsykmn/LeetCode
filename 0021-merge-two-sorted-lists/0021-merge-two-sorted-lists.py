# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1, p2 = list1, list2
        lst = ListNode(None)
        curr = lst
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = ListNode(p1.val)
                p1, curr = p1.next, curr.next
            elif p1.val > p2.val:
                curr.next = ListNode(p2.val)
                p2, curr = p2.next, curr.next
        curr.next = p1 or p2
        return lst.next