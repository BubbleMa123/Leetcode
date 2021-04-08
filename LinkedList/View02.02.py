#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 6:12 下午
# @Author  : MaJiong
# @File    : View02.02.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast, slow = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        return slow.val
