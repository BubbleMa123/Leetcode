#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 2:41 下午
# @Author  : MaJiong
# @File    : Offer_39.py
# @Software: PyCharm
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = major = 0
        for x in nums:
            if vote == 0:
                major = x
            vote += 1 if major == x else -1
        return major


s = Solution()
print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
