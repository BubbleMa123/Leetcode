#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 8:11 下午
# @Author  : MaJiong
# @File    : Offer_24.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre_head = ListNode(-1)
        pre_head.next = head
        pre, p = head, head.next
        while p:
            pre.next = p.next
            p.next = pre_head.next
            pre_head.next = p
            p = pre.next
        return pre_head.next
