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
        # check if they are empty or not
        if not list1 or not list2:
            return list1 or list2
        
        # check which listnode has bigger val
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # redo
        # head = ListNode()
        # current = head
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         current.next = list1
        #         list1 = list1.next
        #     else:
        #         current.next = list2
        #         list2 = list2.next
        #     current = current.next
        # current.next = list1 or list2
        # return head.next