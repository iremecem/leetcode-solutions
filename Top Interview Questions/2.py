"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        car = 0
        ltotal = ListNode()
        cur = ltotal
        while l1 != None or l2 != None or car != 0:
            dig1 = 0
            dig2 = 0
            if l1 != None:
                dig1 = l1.val
                l1 = l1.next
            if l2 != None:
                dig2 = l2.val
                l2 = l2.next
            digit = (dig1 + dig2 + car) % 10
            car = int((dig1 + dig2 + car) / 10)
            cur.next = ListNode(digit)
            cur = cur.next
            
        return ltotal.next