#60 ms, faster than 97.89% of Python3 online submissions for Add Two Numbers
#14.2 MB, less than 99.99% of Python3 online submissions for Add Two Numbers.
#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order, and each of their nodes contains a single digit.
#Add the two numbers and return the sum as a linked list.

#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = l2
        while l1 != None or l2 != None:
            if l1 == None:
                return start 
            if l2.next == None and l1.next != None:
                l2.next = ListNode()
            elif l2.next != None and l1.next == None:
                l1.next = ListNode()
    
            l2.val += l1.val 
            if l2.val > 9:
                l2.val = l2.val% 10
                #carry 
                if l2.next == None:
                    l2.next = ListNode(1)
                else:
                    l2.next.val += 1
            l1, l2 = l1.next,l2.next
        return start
        