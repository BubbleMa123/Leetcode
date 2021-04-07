#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 2:53 下午
# @Author  : MaJiong
# @File    : Offer_40.py
# @Software: PyCharm
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[0:k]


s = Solution()
print(s.getLeastNumbers(arr=[3, 2, 1], k=2))
