#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 2:27 下午
# @Author  : MaJiong
# @File    : Offer_25.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_head = ListNode(-1)
        p = res_head
        while l1 and l2:
            if l1.val < l2.val:
                p.next, l1 = l1, l1.next
            else:
                p.next, l2 = l2, l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return res_head.next


pre_head1 = ListNode(-1)
pre_head2 = ListNode(-1)
p1 = pre_head1
p2 = pre_head2
l1 = [1, 2, 3]
l2 = [1, 3, 4, 5]
for x in l1:
    node = ListNode(x)
    p1.next = node
    p1 = p1.next
for x in l2:
    node = ListNode(x)
    p2.next = node
    p2 = p2.next
s = Solution()
head = s.mergeTwoLists(pre_head1.next, pre_head2.next)
while head:
    print(head.val)
    head = head.next
