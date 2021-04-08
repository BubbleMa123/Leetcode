#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 1:00 下午
# @Author  : MaJiong
# @File    : Offer_52.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         pa, pb = headA, headB
#         while pa and pb:
#             pa = pa.next
#             pb = pb.next
#         if pa:
#             prea = headA
#             while pa:
#                 prea, pa = prea.next, pa.next
#             pa, pb = prea, headB
#         else:
#             preb = headB
#             while pb:
#                 preb, pb = preb.next, pb.next
#             pa, pb = headA, preb
#         while pa != pb:
#             pa, pb = pa.next, pb.next
#         return pa

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_a, node_b = headA, headB
        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else headA
        return node_a
