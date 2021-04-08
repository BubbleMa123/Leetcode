#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 6:23 下午
# @Author  : MaJiong
# @File    : Leco876.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow


class Create:
    def createList(self, val_list):
        pre_head = ListNode(-1)
        p = pre_head
        for x in val_list:
            node = ListNode(x)
            p.next = node
            p = p.next
        return pre_head.next


create = Create()
head = create.createList([1, 2, 3, 4, 5, 6])
s = Solution()
node = s.middleNode(head)
while node:
    print(node.val)
    node = node.next
