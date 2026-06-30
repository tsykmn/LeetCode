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
        node = ListNode(-1)
        current = node

        while list1 and list2:
            if list1.val == list2.val:
                node.next = ListNode(list1.val, ListNode(list2.val))
                node = node.next.next
                list1 = list1.next
                list2 = list2.next
            elif list1.val < list2.val:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next
            elif list1.val > list2.val:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next
        
        node.next = list1 if list1 else list2
        return current.next