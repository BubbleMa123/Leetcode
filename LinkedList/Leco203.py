#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 6:35 下午
# @Author  : MaJiong
# @File    : Leco203.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre_head = ListNode()
        pre_head.next = head
        pre, p = pre_head, head
        while p:
            if p.val == val:
                pre.next, p = p, p.next
            else:
                pre, p = pre.next, p.next
        return pre_head.next
