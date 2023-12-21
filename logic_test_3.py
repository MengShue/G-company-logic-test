#!/usr/bin/python
# -*- coding: utf-8 -*-

def calculate_order(n):
    if n % 3 == 0 and n != 0:
        n = n - 1
    quotient = int(n / 3)
    remainder = n % 3
    return str(quotient * 2 + remainder)

if __name__ == '__main__':
    print("python file is running directly")
    print("order is " + calculate_order(10))