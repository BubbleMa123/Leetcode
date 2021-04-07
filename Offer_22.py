#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 8:07 下午
# @Author  : MaJiong
# @File    : Offer_22.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pre = head
        for i in range(k):
            pre = pre.next
        p = head
        while pre:
            pre = pre.next
            p = p.next
        return p


# class Solution:
#     def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
#         former, latter = head, head
#         for _ in range(k):
#             if not former: return
#             former = former.next
#         while former:
#             former, latter = former.next, latter.next
#         return latter
