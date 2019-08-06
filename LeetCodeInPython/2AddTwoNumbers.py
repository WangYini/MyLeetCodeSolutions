# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        return_list = ListNode(0)
        current = return_list
        carry = 0
        while l1 or l2 or carry:
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            sum = x + y + carry
            carry = int(sum/10)
            current.next = ListNode(sum % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return return_list.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l4 = None
a = Solution()
a.addTwoNumbers(l1,l2)
print(l3.val)
print(l3.next.val)
print(l3.next.next.val)
