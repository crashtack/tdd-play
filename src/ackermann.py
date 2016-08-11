# -*- coding: utf-8 -*-
'''
    This is a doc string
'''

# def ackermann(m, n):
#     return n + 1


def ackermann(m, n):
    # print(u'hello')
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
